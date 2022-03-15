FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8

RUN apk --update add --no-cache nginx

WORKDIR /src

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY start.sh src ./

EXPOSE 80

RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]
