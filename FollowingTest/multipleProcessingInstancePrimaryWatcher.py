import multiprocessing
import MetaTrader5 as mt5
import time
from time import sleep
from multiprocessing import Pool

# MT5终端路径(根据实际安装位置修改)
MT5_PATH = r"C:\Program Files\MetaTrader 5\terminal64.exe"

# 账户配置列表
ACCOUNTS = [
    {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
    {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
    {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
    {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
     {"login": 76898675, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76927664, "password": "Dhj102327!", "server": "Exness-MT5Trial5"},
    {"login": 76890465, "password": "General!23", "server": "Exness-MT5Trial5"},
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
    sleep(10)
    
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
        "type": mt5.ORDER_TYPE_SELL,
        "price": price,
        "deviation": 10,
        "magic": 100,
        "comment": "Python多进程脚本交易",
    }
    result = mt5.order_send(request)
    print(f"订单结果: {result}")
    mt5.shutdown()

def run_account(account):
    """包装交易进程函数"""
    try:
        trade_process(account, f"MT5_Config_{account['login']}")
        return {"status": "success", "account": account["login"]}
    except Exception as e:
        return {"status": "failed", "account": account["login"], "error": str(e)}

def monitor_callback(result):
    """监控回调函数"""
    if result["status"] == "success":
        print(f"账户 {result['account']} 交易进程完成")
    else:
        print(f"账户 {result['account']} 失败: {result['error']}")

if __name__ == "__main__":
    with Pool(processes=40) as pool:
        # 异步提交任务
        async_results = [
            pool.apply_async(
                run_account, 
                args=(account,), 
                callback=monitor_callback
            ) for account in ACCOUNTS
        ]
        
        # 持续监控
        while True:
            time.sleep(5)
            alive = sum(1 for r in async_results if not r.ready())
            print(f"活跃进程数: {alive}/{len(ACCOUNTS)}")
            
            if all(r.ready() for r in async_results):
                print("所有进程已完成")
                break
