# network/http_health_checker.py

import requests

RESPONSE_TIME_THRESHOLD = 1.0  # seconds

urls = [
    "https://google.com",
    "https://github.com",
    "https://httpbin.org/status/500",
    "https://example.com",
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)

        status_code = response.status_code
        response_time = response.elapsed.total_seconds()

        print(
            f"{url:<35} "
            f"Status: {status_code} "
            f"Time: {response_time:.3f}s"
        )

        if status_code != 200:
            print(
                f"  ALERT: Unexpected status code ({status_code})"
            )

        if response_time > RESPONSE_TIME_THRESHOLD:
            print(
                f"  ALERT: Slow response ({response_time:.3f}s)"
            )

    except requests.exceptions.Timeout:
        print(f"{url:<35} ALERT: Request timed out")

    except requests.exceptions.ConnectionError:
        print(f"{url:<35} ALERT: Connection failed")

    except requests.exceptions.RequestException as e:
        print(f"{url:<35} ALERT: {e}")
