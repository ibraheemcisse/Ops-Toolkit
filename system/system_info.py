import platform
import socket
import psutil

def system_info():
    # 1. Collect the pieces
    hostname = socket.gethostname()
    os_name = platform.system()
    kernel_version = platform.release()
    architecture = platform.machine()
    cpu_cores = psutil.cpu_count()
    
    # Calculate RAM in GB (bytes -> KB -> MB -> GB)
    total_ram_bytes = psutil.virtual_memory().total
    total_ram_gb = round(total_ram_bytes / (1024 ** 3), 2)

    # 2. Print in a readable format
    print("===== System Information =====")
    print(f"Hostname: {hostname}")
    print(f"OS: {os_name}")
    print(f"Kernel Version: {kernel_version}")
    print(f"Architecture: {architecture}")
    print(f"CPU Cores: {cpu_cores}")
    print(f"Total RAM: {total_ram_gb} GB")
    print("==============================")

# Run the function
system_info()
