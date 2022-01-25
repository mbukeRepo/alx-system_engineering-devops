#!/usr/bin/env bash
#configures our servers

apt update
apt install -y nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
