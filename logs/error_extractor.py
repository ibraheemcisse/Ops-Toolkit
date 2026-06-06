import sys
from datetime import datetime
sys.path.insert(0, '/home/ubuntu/ops-toolkit')
from utils.alerting import send_alert

def extract_errors(log_file="/tmp/app.log"):
    error_count = 0
    critical_count = 0
    with open(log_file, "r") as file:
        for line in file:
            line = line.strip()
            if "ERROR" in line:
                error_count += 1
            if "CRITICAL" in line:
                critical_count += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{timestamp}] ===== Log Summary =====")
    print(f"ERROR entries:    {error_count}")
    print(f"CRITICAL entries: {critical_count}")
    print("=======================")
    if critical_count > 0:
        send_alert("CRITICAL", "error_extractor", f"{critical_count} CRITICAL entries found in {log_file}")

extract_errors()
