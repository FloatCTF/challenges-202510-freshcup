FROM php:5-apache-jessie

LABEL Author="ablklice <ablklice@gmail.com>"

COPY ./files /tmp/
RUN cp -rf /tmp/html /var/www/ \
    && cp -f /tmp/flag.sh /flag.sh \
    && chown -R www-data:www-data /var/www/html \
    && chmod +x /flag.sh
    
WORKDIR /var/www/html

CMD ["sh", "-c", "/flag.sh && apache2-foreground"]