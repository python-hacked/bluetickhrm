[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/bluetickhrm/hrmanagement
ExecStart=/home/ubuntu/bluetickhrm/hrmanagement/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/bluetickhrm/hrmanagement.sock hrmanagement/hrmanagement.wsgi:application

[Install]
WantedBy=multi-user.target