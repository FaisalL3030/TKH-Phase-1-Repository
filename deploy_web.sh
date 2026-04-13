#!/bin/bash
# ================================================================
# ARTIFACT: deploy_web.sh
# MISSION: S11 - The Container Revolution
# OPERATOR: Faisal
# TARGET IP: 192.168.252.128
# ================================================================

echo "[+] Initializing Disposable Web Server..."

# Step 2: Launch the Nginx container in detached mode
# Mapping Host Port 8080 to Container Port 80
docker run -d --name training-web -p 8080:80 nginx

echo "[+] Deployment Successful."
echo "[+] Target URL: http://192.168.252.128:8080"

# Step 3: Automated modification of the index page
docker exec training-web bash -c "echo 'Titan Security Training' > /usr/share/nginx/html/index.html"

echo "[+] Content Modified: 'Titan Security Training' is live."
echo "[+] Audit Logs:"
docker logs training-web
