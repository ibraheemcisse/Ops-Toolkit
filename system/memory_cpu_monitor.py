import psutil
import sys
from datetime import datetime
sys.path.insert(0, '/home/ubuntu/ops-toolkit')
from utils.alerting import send_alert

def check_memory(threshold=80):
    memory = psutil.virtual_memory()
    percent_used = memory.percent
    total_gb = round(memory.total / 1024**3, 2)
    used_gb = round(memory.used / 1024**3, 2)
    available_gb = round(memory.available / 1024**3, 2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if percent_used >= threshold:
        print(f"[{timestamp}] CRITICAL: Memory usage is {percent_used}% ({used_gb}GB used of {total_gb}GB)")
        send_alert("CRITICAL", "memory_monitor", f"Memory usage is {percent_used}%")
        return False
    else:
        print(f"[{timestamp}] OK: Memory usage is {percent_used}% ({used_gb}GB used of {total_gb}GB, {available_gb}GB available)")
        return True

def check_cpu(threshold=80):
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if cpu_percent >= threshold:
        print(f"[{timestamp}] CRITICAL: CPU usage is {cpu_percent}% across {cpu_count} cores")
        send_alert("CRITICAL", "cpu_monitor", f"CPU usage is {cpu_percent}%")
        return False
    else:
        print(f"[{timestamp}] OK: CPU usage is {cpu_percent}% across {cpu_count} cores")
        return True

check_memory()
check_cpu()
