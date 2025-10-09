FROM php:7.4-apache
LABEL Author="myx2727461997@gmail.com"

# 复制网站文件
COPY index.php /var/www/html/

WORKDIR /var/www/html

EXPOSE 80

# flag替换脚本 固定， 剔除\r
COPY flag.sh /flag.sh
RUN [ -f /flag.sh ] && tr -d '\r' < /flag.sh | tee /flag.sh >/dev/null && chmod +x /flag.sh
# flag replacer script end
# 启动 Apache 并保持前台运行
CMD ["bash", "-c", "/flag.sh && apache2-foreground"]
