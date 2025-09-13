FROM nginx:alpine
LABEL Author="myx2727461997@gmail.com"

# 复制网站文件
COPY index.html /usr/share/nginx/html/
COPY robots.txt /usr/share/nginx/html/
COPY s3cr3t_b4ckd00r.html /usr/share/nginx/html/
COPY flag.sh /flag.sh
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 设置权限并执行 flag 脚本
RUN chmod +x /flag.sh && sh /flag.sh

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]