import subprocess
import sys
sys.path.insert(0, '/home/ubuntu/ops-toolkit')
from utils.alerting import send_alert

result = subprocess.run(
    ["free", "-h"],
    capture_output=True,
    text=True
)

print(result.stdout)

lines = result.stdout.strip().split("\n")
mem_line = lines[1].split()
total = mem_line[1]
used = mem_line[2]
available = mem_line[6]

print(f"Memory - Total: {total} | Used: {used} | Available: {available}")

# Convert to check percentage
# free -m gives numbers without Mi suffix - easier to calculate
result2 = subprocess.run(
    ["free", "-m"],
    capture_output=True,
    text=True
)
lines2 = result2.stdout.strip().split("\n")
mem_line2 = lines2[1].split()
total_mb = int(mem_line2[1])
used_mb = int(mem_line2[2])
percent_used = int((used_mb / total_mb) * 100)

print(f"Memory usage: {percent_used}%")

if percent_used >= 80:
    send_alert("CRITICAL", "memory_monitor", f"Memory usage is {percent_used}%")
else:
    print(f"OK: Memory usage is {percent_used}%")
