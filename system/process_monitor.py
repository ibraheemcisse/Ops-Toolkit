import subprocess
import sys
from datetime import datetime

sys.path.insert(0, '/home/ubuntu/ops-toolkit')

from utils.alerting import send_alert


def check_process(process_name):
    result = subprocess.run(
        ["pgrep", "-f", process_name],
        capture_output=True,
        text=True
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if result.returncode == 0:
        print(f"[{timestamp}] OK: {process_name} is running")
        return True
    else:
        print(f"[{timestamp}] CRITICAL: {process_name} is not running")
        send_alert(
            "CRITICAL",
            "process_monitor",
            f"{process_name} is not running"
        )
        return False


processes = ["nginx", "sshd", "systemd"]

for process in processes:
    check_process(process)
