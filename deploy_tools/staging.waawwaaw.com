server {
    listen 80;
    server_name staging.waawwaaw.com;

    location /static {
        alias /home/ardila/sites/staging.waawwaaw.com/static;
    }

    location / {
        proxy_set_header Host $host;
        proxy_pass http://unix:/tmp/staging.waawwaaw.com.socket;
    }
}
