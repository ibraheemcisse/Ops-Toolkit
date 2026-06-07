import os
import sys
import datetime

if len(sys.argv) != 2:
    print("Usage: python log_rotation_checker.py <log_directory>")
    sys.exit(1)

log_dir = sys.argv[1]

for filename in os.listdir(log_dir):
    filepath = os.path.join(log_dir, filename)

    # Skip directories
    if not os.path.isfile(filepath):
        continue

    modified_time = os.path.getmtime(filepath)
    modified_date = datetime.datetime.fromtimestamp(modified_time)

    age_days = (datetime.datetime.now() - modified_date).days
    size_bytes = os.path.getsize(filepath)

    if age_days > 7:
        print(
            f"{filename} | "
            f"Age: {age_days} days | "
            f"Size: {size_bytes} bytes | "
            f"Modified: {modified_date}"
        )
