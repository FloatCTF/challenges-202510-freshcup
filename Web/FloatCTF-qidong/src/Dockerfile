FROM nginx:1.25-alpine

LABEL maintainer="FloatCTF <myx2727461997@gmail.com>"

WORKDIR /usr/share/nginx/html

COPY index.html ./
COPY result.html ./
COPY app.js ./
COPY style.css ./
EXPOSE 80

# flag替换脚本 固定， 剔除\r
COPY flag.sh /flag.sh
RUN [ -f /flag.sh ] && tr -d '\r' < /flag.sh | tee /flag.sh >/dev/null && chmod +x /flag.sh
# flag replacer script end
# 启动 Apache 并保持前台运行
CMD ["/bin/sh", "-c", "/flag.sh && nginx -g 'daemon off;'"]