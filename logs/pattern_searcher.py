# logs/pattern_searcher.py

import sys

if len(sys.argv) < 3:
    print("Usage: python pattern_searcher.py <pattern> <file1> [file2 ...]")
    sys.exit(1)

pattern = sys.argv[1]
log_files = sys.argv[2:]

for filename in log_files:
    try:
        with open(filename, "r") as f:
            for line in f:
                if pattern in line:
                    print(f"{filename}: {line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: {filename} not found")
