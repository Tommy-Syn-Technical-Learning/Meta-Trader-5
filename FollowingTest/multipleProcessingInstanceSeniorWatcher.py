import multiprocessing
import MetaTrader5 as mt5
import time
from time import sleep
from multiprocessing import Pool, current_process

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

class MonitoringPool(Pool):
    """可监控的进程池子类"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._task_status = {}
    
    def apply_async(self, func, args=(), kwargs={}, callback=None):
        """重写apply_async以添加监控"""
        pid = current_process().pid
        self._task_status[pid] = {"start": time.time(), "status": "running"}
        
        def wrapped_callback(result):
            self._task_status[pid]["end"] = time.time()
            self._task_status[pid]["status"] = "completed"
            if callback:
                callback(result)
        
        return super().apply_async(
            func, args=args, kwargs=kwargs, callback=wrapped_callback
        )
    
    def get_status(self):
        """获取当前进程状态"""
        return self._task_status

def monitor_pool(pool):
    """监控线程函数"""
    while True:
        time.sleep(10)
        status = pool.get_status()
        print("\n===== 进程监控报告 =====")
        for pid, info in status.items():
            runtime = info.get("end", time.time()) - info["start"]
            print(f"PID {pid}: {info['status']} | 运行时间: {runtime:.1f}s")
        print("="*30)

if __name__ == "__main__":
    with MonitoringPool(processes=20) as pool:
        # 启动监控线程
        import threading
        monitor_thread = threading.Thread(
            target=monitor_pool, args=(pool,), daemon=True
        )
        monitor_thread.start()
        
        # 提交任务
        pool.map(run_account, ACCOUNTS)
        
        # 等待所有任务完成
        pool.close()
        pool.join()

