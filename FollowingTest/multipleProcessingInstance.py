import multiprocessing
import MetaTrader5 as mt5
from time import sleep

# MT5终端路径(根据实际安装位置修改)
MT5_PATH = r"C:\Program Files\MetaTrader 5\terminal64.exe"

# 账户配置列表
ACCOUNTS = [
    {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
]

def trade_process(account, config_dir):
    """
    单个交易进程函数
    :param account: 账户信息字典
    :param config_dir: MT5配置目录
    """
    # 启动MT5实例
    import subprocess
    args = [
        MT5_PATH,
        f"/config:{config_dir}",
        f"/login:{account['login']}",
        f"/password:{account['password']}",
        f"/server:{account['server']}",
    ]
    subprocess.Popen(args)
    
    # 等待MT5初始化
    sleep(30)
    
    # 连接到MT5
    if not mt5.initialize(login=account["login"], 
                         password=account["password"],
                         server=account["server"]):
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
        "comment": "Python多进程脚本交易",
    }
    result = mt5.order_send(request)
    print(f"订单结果: {result}")
    mt5.shutdown()

if __name__ == "__main__":
    # 创建并启动多个交易进程
    processes = []
    for i, account in enumerate(ACCOUNTS):
        config_dir = f"MT5_Config_{i+1}"
        p = multiprocessing.Process(
            target=trade_process,
            args=(account, config_dir),
            name=f"MT5_Trader_{account['login']}"
        )
        p.start()
        processes.append(p)
        print(f"启动进程交易账户: {account['login']}")
    
    # 等待所有进程完成(通常不会执行到这里，因为交易进程是持续运行的)
    for p in processes:
        p.join()