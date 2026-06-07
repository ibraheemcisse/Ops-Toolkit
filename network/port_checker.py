import socket
import sys


def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except Exception:
        return False


# Bulk check mode
if len(sys.argv) == 1:
    services = [
        ("localhost", 22, "SSH"),
        ("localhost", 80, "HTTP"),
        ("localhost", 443, "HTTPS"),
        ("8.8.8.8", 53, "DNS"),
        ("google.com", 443, "Google"),
    ]

    for host, port, name in services:
        if check_port(host, port):
            print(f"OK    {name} ({host}:{port})")
        else:
            print(f"FAIL  {name} ({host}:{port})")

    sys.exit(0)


if len(sys.argv) != 3:
    print("Usage: python port_checker.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]

try:
    port = int(sys.argv[2])
except ValueError:
    print("Error: port must be an integer")
    sys.exit(1)

try:
    with socket.create_connection((host, port), timeout=3):
        print(f"{host}:{port} is OPEN")

except socket.timeout:
    print(f"{host}:{port} is CLOSED (connection timed out)")

except ConnectionRefusedError:
    print(f"{host}:{port} is CLOSED (connection refused)")

except socket.gaierror:
    print(f"Error: could not resolve hostname '{host}'")

except OSError as e:
    print(f"{host}:{port} is CLOSED or unreachable ({e})")
