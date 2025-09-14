set -o errexit
#poetry install
#pip install gunicorn
#pip install dj-database-url
#pip install whitenoise
#pip install autopep8
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate