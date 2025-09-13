FROM php:7.4-apache
LABEL Author="myx2727461997@gmail.com"

# 复制网站文件
COPY index.php /var/www/html/
COPY flag.sh /flag.sh

# 转换行结束符并设置权限
RUN sed -i 's/\r$//' /flag.sh && chmod +x /flag.sh

WORKDIR /var/www/html

EXPOSE 80

# 在容器启动时执行 flag 替换，然后启动 Apache
CMD ["/bin/bash", "-c", "/flag.sh && apache2-foreground"]