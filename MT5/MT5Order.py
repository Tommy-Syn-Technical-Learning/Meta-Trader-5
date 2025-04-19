import MetaTrader5 as mt5
import pandas as pd
import os
from datetime import datetime
 
# Set the proxy environment variables
os.environ['HTTP_PROXY'] = 'http://your-proxy-server:port'
os.environ['HTTPS_PROXY'] = 'http://your-proxy-server:port'

# ================================
# 1. 初始化并登录 MT5
# ================================
def login_mt5():
    print("🔐 请登录到 MetaTrader 5")
    login = int(input("请输入账号: "))
    password = input("请输入密码: ")
    server = input("请输入服务器名称 (例如: ICMarkets-Demo): ")
    
    # 初始化 MT5
    if not mt5.initialize(login=login, password=password, server=server):
        print(f"❌ MT5 初始化失败，错误代码: {mt5.last_error()}")
        quit()

    # 登录 MT5
    if not mt5.login(login, password, server):
        print(f"❌ 登录失败，错误代码: {mt5.last_error()}")
        quit()

    print(f"✅ 成功连接到账户：{login}")
    return True


# ================================
# 2. 获取账户信息
# ================================
def get_account_info():
    account_info = mt5.account_info()
    if account_info is None:
        print("❌ 无法获取账户信息")
    else:
        print(f"💰 账户余额: {account_info.balance}")
        print(f"📊 账户杠杆: {account_info.leverage}")
        print(f"⚡ 账户权益: {account_info.equity}")


# ================================
# 3. 获取市场数据
# ================================
def get_market_data(symbol="EURUSDm"):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"❌ {symbol} 不存在，请检查品种名称")
        return

    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"❌ 无法获取 {symbol} 的报价")
        return

    print(f"📈 {symbol} 市场报价: Bid={tick.bid}, Ask={tick.ask}, Time={datetime.fromtimestamp(tick.time)}")


# ================================
# 4. 获取历史数据
# ================================
def get_history_data(symbol="EURUSDm", timeframe=mt5.TIMEFRAME_M1, count=100):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)
    if rates is None or len(rates) == 0:
        print(f"❌ 无法获取 {symbol} 的历史数据")
        return

    # 转换为 pandas DataFrame
    rates_frame = pd.DataFrame(rates)
    rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
    print(f"📊 {symbol} 最近 {count} 根 K 线数据：")
    print(rates_frame.tail(10))


# ================================
# 5. 下单交易
# ================================
def create_order(symbol, action, volume, price=None, sl=None, tp=None):


    # 如果没有提供价格，则使用市场价格
    if price is None:
        tick = mt5.symbol_info_tick(symbol)
        if tick is None:
            print(f"❌ 无法获取 {symbol} 的市场报价")
            return False
        price = tick.ask if action.lower() == "buy" else tick.bid
        print("ask:",tick.ask)
        print("tick",tick)
    point = mt5.symbol_info(symbol).point
    if action.lower() == "buy":
        order_type = mt5.ORDER_TYPE_BUY
        sl = price - 1000 * point
        tp = price + 1000 * point
    elif action.lower() == "sell":
        order_type = mt5.ORDER_TYPE_SELL
        sl = price + 1000 * point
        tp = price - 1000 * point
    else:
        print("⚠️ 无效的交易类型，请使用 'buy' 或 'sell'")
        return False
    print("point",point)
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 123456,
        "comment": "Python Order",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    print(f"create request: {request}")
    result = mt5.order_send(request)
    print("error: ",mt5.last_error())
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"❌ 订单执行失败，错误代码: {result}")
        return False
    print(f"✅ 订单执行成功！订单编号: {result.order}")
    return result.order
    


# ================================
# 6. 查看当前持仓
# ================================
def get_positions():
    positions = mt5.positions_get()
    if positions is None or len(positions) == 0:
        print("📭 没有持仓")
        return

    for pos in positions:
        print(f"📊 品种: {pos.symbol}, 交易量: {pos.volume}, 持仓类型: {'买入' if pos.type == 0 else '卖出'}, 盈亏: {pos.profit}")


# ================================
# 7. 撤销订单
# ================================
def cancel_order(order_id):
    order = mt5.orders_get(ticket=order_id)
    if order is None:
        print(f"❌ 找不到订单号: {order_id}")
        return

    request = {
        "action": mt5.TRADE_ACTION_REMOVE,
        "order": order_id,
    }
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"❌ 订单撤销失败，错误代码: {result.retcode}")
    else:
        print(f"✅ 订单撤销成功！订单号: {order_id}")


# ================================
# 8. 主菜单
# ================================
def main_menu():
    while True:
        print("\n==============================")
        print("📡 MetaTrader 5 终端")
        print("1️⃣  获取账户信息")
        print("2️⃣  获取市场数据 (EURUSDm)")
        print("3️⃣  获取历史数据 (EURUSDm, M1, 100根)")
        print("4️⃣  查看当前持仓")
        print("5️⃣  创建订单 (XAUUSDm/EURUSDm)")
        print("6️⃣  撤销订单")
        print("❌  输入 'q' 退出程序")
        print("==============================")

        choice = input("👉 请选择操作 (1/2/3/4/5/6/q): ").strip()

        if choice == "1":
            get_account_info()
        elif choice == "2":
            get_market_data()
        elif choice == "3":
            get_history_data()
        elif choice == "4":
            get_positions()
        elif choice == "5":
            symbol = input("👉 请输入交易品种 (EURUSDm/XAUUSDm): ").strip()
            action = input("👉 请输入交易类型 (buy/sell): ").strip().lower()
            volume = float(input("👉 请输入交易量: ").strip())
            create_order(symbol, action, volume)
        elif choice == "6":
            order_id = int(input("👉 请输入要撤销的订单号: ").strip())
            cancel_order(order_id)
        elif choice.lower() == "q":
            print("👋 退出程序，正在关闭连接...")
            mt5.shutdown()
            break
        else:
            print("⚠️  无效输入，请重新选择")


# ================================
# 9. 程序入口
# ================================
if __name__ == "__main__":
    if login_mt5():
        main_menu()