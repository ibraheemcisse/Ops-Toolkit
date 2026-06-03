# ops-toolkit

Production-grade operational scripts for Linux system administration,
infrastructure monitoring, and Kubernetes operations.

Built as daily-use tooling for SRE and platform engineering workflows.
No external dependencies beyond Python standard library and boto3.

## Scripts

### System Health
- `system/disk_check.py` — monitor disk usage, alert above threshold
- `system/memory_cpu_monitor.py` — snapshot and log memory and CPU state
- `system/process_monitor.py` — verify critical processes, restart if down
- `system/system_info.py` — full system report in one command

### Log Analysis
- `logs/error_extractor.py` — parse log files, count and summarize errors
- `logs/log_rotation_checker.py` — find logs older than N days, report size
- `logs/pattern_searcher.py` — search strings across multiple log files

### Network
- `network/port_checker.py` — check host/port reachability
- `network/latency_monitor.py` — ping hosts, report response times
- `network/http_health_checker.py` — hit URLs, report status codes

### Automation
- `automation/ssh_command_runner.py` — run commands on remote servers
- `automation/file_sync_checker.py` — compare directories, report differences
- `automation/backup_script.py` — compress, timestamp, move to backup location

### Infrastructure
- `infrastructure/cluster_health_checker.py` — Kubernetes node and pod status
- `infrastructure/gpu_utilization_logger.py` — log VRAM and GPU utilization
- `infrastructure/ec2_cost_estimator.py` — list EC2 instances, calculate cost

## Usage

\`\`\`bash
python3 system/disk_check.py
python3 network/port_checker.py --host 10.0.1.70 --port 6443
\`\`\`

## Environment

Tested on Ubuntu 22.04, Python 3.10+
