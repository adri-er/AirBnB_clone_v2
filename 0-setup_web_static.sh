#!/usr/bin/env bash
# Create script to set up a web server
sudo apt-get update
sudo apt-get install nginx -y
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Fake content" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
