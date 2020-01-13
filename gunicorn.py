bind = 'unix:/tmp/gunicorn_app.sock'
backlog = 2048

daemon = False
raw_env = [
    'DJANGO_SETTINGS_MODULE=core.settings_dev',
    'DB_HOST=localhost',
    "DB_PASSWORD=&*u:90OP"
]
