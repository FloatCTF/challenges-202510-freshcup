FROM nginx:1.25-alpine

LABEL maintainer="FloatCTF <myx2727461997@gmail.com>"

WORKDIR /usr/share/nginx/html

COPY index.html ./
COPY result.html ./
COPY app.js ./
COPY style.css ./
COPY flag.sh /flag.sh
RUN chmod +x /flag.sh

EXPOSE 80

CMD ["/bin/sh", "-c", "/flag.sh && nginx -g 'daemon off;'"]
