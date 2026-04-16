# TITAN SMALL BUSINESS SERVICES: SECURITY ARCHITECTURE DOCUMENT (SAD)
**Operator:** [Faisal Larry]
**Date:** [April 15th 2026]

## 1. Perimeter Hardening (UFW & SSH)
* **SSH Status:** [PermitRootLogin no password authentication no]
* **Firewall Logic:** [sys_auditor.py]

## 2. The Automated Auditor (Python)
* **Script Logic:** [import os

dc_ip = "YOUR_DC_IP_HERE"
log_path = "/var/log/dc_audit.log"

disk_stats = os.popen('df -h').read()
ping_check = os.system(f"ping -c 4 {dc_ip} > /dev/null 2>&1")
status = "DC is UP" if ping_check == 0 else "DC is DOWN"

with open(log_path, "a") as f:
    f.write(f"Status: {status}\n{disk_stats}\n")
]
* **Telemetry Path:** `/var/log/sys_audit.log`

## 3. Containerized App (Docker)
* **Network Isolation:** [By using this "air-gap" strategy and not exposing any ports for the database, we ensured that the container is not reachable from the host machine or any external connections]
* **Stack Health:** [version: '3.8'

services:
  wiki:
    image: nginx
    ports:
      - "8080:80"
    networks:
      - frontend
      - backend

  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: password
    networks:
      - backend

networks:
  frontend:
  backend:
    internal: true
]

## 4. Executive Summary
[We made a locked perimeter by stopping remote access to digital keys and configuring a firewall that denies all traffic except for a few specific  points. Also  we used network isolation to air-gap the database from external threats while using an automated Python script to monitor the system.]
