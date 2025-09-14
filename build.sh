set -o errexit
#poetry install
pip install -r requiremenst.txt
#pip install gunicorn
#pip install dj-database-url
#pip install whitenoise
#pip install autopep8
python manage.py collectstatic --noinput
python manage.py migrate