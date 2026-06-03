from datetime import datetime
import subprocess

def check_disk_space(path="/", threshold=90):
    result = subprocess.run(
        ["df", "-h", path],
        capture_output=True,
        text=True
    )
    lines = result.stdout.strip().split("\n")
    usage_line = lines[1].split()
    usage_percent = int(usage_line[4].replace("%", ""))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if usage_percent >= threshold:
        print(f"[{timestamp}] CRITICAL: {path} usage is {usage_percent}%")
        return False
    else:
        print(f"[{timestamp}] OK: {path} usage is {usage_percent}%")
        return True

paths = ["/", "/tmp", "/home"]

for path in paths:
    check_disk_space(path)
