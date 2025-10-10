FROM php:5-apache-jessie
LABEL Author="ablklice <ablklice@gmail.com>"

COPY index.php /var/www/html/index.php
COPY key.php /var/www/html/key.php

COPY flag.sh /flag.sh
RUN chmod 755 /flag.sh && \
    chown www-data:www-data /flag.sh


WORKDIR /var/www/html

# 启动 Apache 并保持前台运行
CMD ["sh", "-c", "/flag.sh && apache2-foreground"]