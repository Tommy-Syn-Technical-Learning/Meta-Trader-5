import subprocess
import time
import MetaTrader5 as mt5

# MT5 终端路径（需替换为你的实际路径）
MT5_PATH = r"C:\Program Files\MetaTrader 5\terminal64.exe"

# 账户列表（账号、密码、服务器）
ACCOUNTS = [
    {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
]

def launch_mt5_instance(config_dir, account):
    """
    启动一个 MT5 实例并自动登录
    :param config_dir: 实例配置目录（如 Config1）
    :param account: 账户信息（login, password, server）
    """
    args = [
        MT5_PATH,
        f"/config:{config_dir}",  # 独立配置目录
        f"/login:{account['login']}",
        f"/password:{account['password']}",
        f"/server:{account['server']}",
    ]
    subprocess.Popen(args)
    print(f"MT5 实例已启动: {config_dir}, 账户: {account['login']}")

def get_positions():
    positions = mt5.positions_get()
    if positions is None or len(positions) == 0:
        print("📭 没有持仓")
        return

    for pos in positions:
        print(f"📊 品种: {pos.symbol}, 交易量: {pos.volume}, 持仓类型: {'买入' if pos.type == 0 else '卖出'}, 盈亏: {pos.profit}")

def trade_for_instance(account):
    """
    连接到指定账户并执行交易
    """
    if not mt5.initialize(login=account["login"], password=account["password"], server=account["server"]):
        print(f"账户 {account['login']} 初始化失败，错误代码:", mt5.last_error())
        return
    
    print(f"账户 {account['login']} 已连接，余额:", mt5.account_info().balance)
    
    # 示例：下单（BTCUSDm 买进 0.1 手）
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
        "comment": "Python脚本交易",
    }
    result = mt5.order_send(request)
    print(f"订单结果: {result}")
    get_positions()
    mt5.shutdown()

if __name__ == "__main__":
    # 启动多个 MT5 实例
    for i, account in enumerate(ACCOUNTS):
        config_dir = f"MT5_Instance_{i+1}"  # 为每个实例创建独立配置目录
        launch_mt5_instance(config_dir, account)
    
    # 等待实例初始化（根据实际情况调整延迟）
    time.sleep(30)  
    
    # 为每个账户执行交易
    for account in ACCOUNTS:
        trade_for_instance(account)