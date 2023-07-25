#!/bin/bash
sudo yum update -y
sudo yum install nginx  httpd -y
echo "hello world" >> /var/www/html/index.html
sudo systemctl start httpd
sudo systemctl start nginx
