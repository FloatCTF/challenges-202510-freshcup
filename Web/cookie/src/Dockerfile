FROM php:7.4-apache
LABEL Author="myx2727461997@gmail.com"

# 复制网站文件
COPY index.php /var/www/html/
COPY flag.sh /flag.sh

# 设置权限并执行 flag 脚本
RUN chmod +x /flag.sh && bash /flag.sh

WORKDIR /var/www/html

EXPOSE 80

CMD ["apache2-foreground"]