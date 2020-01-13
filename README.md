## Информация о проекте
Интернет блог

## Использоуемые технологии
- HTML
- CSS
- JavaScript
- python 3.6
- nginx
- gunicorn
- PostgreSQL
- Django Framework

## Информация по установке
- cd /home
- git clone
- cd MarketPeak_blog
- python3 -m venv venv
- . venv/bin/activate
- pip -r requirements.txt
- apt-get insatll supervisor nginx
- прописываем в /etc/nginx/nginx.conf путь к /home/MarketPeak_blog/etc/nginx.conf.
- прописываем в /etc/supervisor/supervisor.conf путь к /home/MarketPeak_blog/etc/supervisor.conf
- service  supervisor start

## Разработали:
- Войтехович П.С.
- Маркварде А.В.
- Бессонова В.А.
