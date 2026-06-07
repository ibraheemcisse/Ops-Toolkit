# network/latency_monitor.py

import subprocess
import re

LATENCY_THRESHOLD = 100  # ms

hosts = [
    "google.com",
    "cloudflare.com",
    "8.8.8.8",
    "1.1.1.1",
]


def get_latency(host):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", host],
            capture_output=True,
            text=True,
            timeout=5,
        )

        if result.returncode != 0:
            return None

        output = result.stdout

        # Example:
        # rtt min/avg/max/mdev = 1.234/5.678/9.012/0.123 ms
        match = re.search(
            r"rtt min/avg/max/(?:mdev|stddev) = [\d.]+/([\d.]+)/",
            output,
        )

        if match:
            return float(match.group(1))

        return None

    except subprocess.TimeoutExpired:
        return None
    except Exception:
        return None


for host in hosts:
    latency = get_latency(host)

    if latency is None:
        print(f"{host:<20} UNREACHABLE")
        continue

    print(f"{host:<20} {latency:.2f} ms")

    if latency > LATENCY_THRESHOLD:
        print(
            f"  ALERT: latency exceeds threshold "
            f"({LATENCY_THRESHOLD} ms)"
        )
