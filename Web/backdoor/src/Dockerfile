FROM php:5-apache-jessie
LABEL Author="fb0sh <fb0sh@outlook.com>"

COPY index.php /var/www/html/index.php
COPY flag /flag

WORKDIR /var/www/html


# flag替换脚本 固定， 剔除\r
COPY flag.sh /flag.sh
RUN [ -f /flag.sh ] && tr -d '\r' < /flag.sh | tee /flag.sh >/dev/null && chmod +x /flag.sh
# flag replacer script end
# 启动 Apache 并保持前台运行
CMD ["bash", "-c", "/flag.sh && apache2-foreground"]
