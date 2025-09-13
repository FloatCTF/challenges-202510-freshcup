FROM nginx:alpine
LABEL Author="myx2727461997@gmail.com"

# 复制网站文件
COPY index.html /usr/share/nginx/html/
COPY robots.txt /usr/share/nginx/html/
COPY s3cr3t_b4ckd00r.html /usr/share/nginx/html/
COPY flag.sh /flag.sh
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 转换行结束符并设置权限
RUN sed -i 's/\r$//' /flag.sh && chmod +x /flag.sh

EXPOSE 80

# 在容器启动时执行 flag 替换，然后启动 nginx
CMD ["/bin/sh", "-c", "/flag.sh && nginx -g 'daemon off;'"]