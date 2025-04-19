import asyncio
import subprocess
import MetaTrader5 as mt5

# MT5 终端路径（需替换为你的路径）
MT5_PATH = r"C:\Program Files\MetaTrader 5\terminal64.exe"

# 账户列表
ACCOUNTS = [
      {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
]

async def launch_mt5_instance(config_dir, account):
    """
    协程：启动一个 MT5 实例并自动登录
    """
    args = [
        MT5_PATH,
        f"/config:{config_dir}",
        f"/login:{account['login']}",
        f"/password:{account['password']}",
        f"/server:{account['server']}",
    ]
    process = await asyncio.create_subprocess_exec(*args)
    print(f"MT5 实例启动: {config_dir}, 账户: {account['login']}")
    return process

async def trade_for_instance(account):
    """
    协程：连接到 MT5 实例并执行交易
    """
    if not mt5.initialize(login=account["login"], password=account["password"], server=account["server"]):
        print(f"账户 {account['login']} 初始化失败，错误代码:", mt5.last_error())
        return

    print(f"账户 {account['login']} 已连接，余额:", mt5.account_info().balance)
    
    # 示例：买入 BTCUSDm 0.1 手
    symbol = "BTCUSDm"
    lot = 0.1
    price = mt5.symbol_info_tick(symbol).ask
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "deviation": 10,
        "magic": 100,
        "comment": "异步协程交易",
    }
    result = mt5.order_send(request)
    print(f"账户 {account['login']} 订单结果: {result}")
    mt5.shutdown()

async def main():
    """
    主协程：并行启动实例并执行交易
    """
    # 异步启动所有 MT5 实例
    tasks_launch = [
        launch_mt5_instance(f"MT5_Instance_{i+1}", account)
        for i, account in enumerate(ACCOUNTS)
    ]
    processes = await asyncio.gather(*tasks_launch)

    # 等待实例初始化（根据需要调整延迟）
    await asyncio.sleep(30)

    # 异步为每个账户执行交易
    tasks_trade = [trade_for_instance(account) for account in ACCOUNTS]
    await asyncio.gather(*tasks_trade)

if __name__ == "__main__":
    asyncio.run(main())