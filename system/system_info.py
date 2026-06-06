import platform
import socket
import psutil
import datetime  # Added new import

def system_info():
    # 1. Collect the pieces
    hostname = socket.gethostname()
    os_name = platform.system()
    kernel_version = platform.release()
    architecture = platform.machine()
    cpu_cores = psutil.cpu_count()
    
    # Calculate RAM in GB
    total_ram_bytes = psutil.virtual_memory().total
    total_ram_gb = round(total_ram_bytes / (1024 ** 3), 2)
    
    # Calculate Uptime
    boot_time = psutil.boot_time()
    uptime_seconds = datetime.datetime.now().timestamp() - boot_time
    uptime = str(datetime.timedelta(seconds=int(uptime_seconds)))

    # 2. Print in a readable format
    print("===== System Information =====")
    print(f"Hostname: {hostname}")
    print(f"OS: {os_name}")
    print(f"Kernel Version: {kernel_version}")
    print(f"Architecture: {architecture}")
    print(f"CPU Cores: {cpu_cores}")
    print(f"Total RAM: {total_ram_gb} GB")
    print(f"Uptime: {uptime}")  # Added new print line
    print("==============================")

# Run the function
system_info()
