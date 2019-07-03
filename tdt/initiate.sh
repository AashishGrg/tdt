rm -f db.sqlite3

rm -rf authentication/migrations/
rm -rf product/migrations/
rm -rf emailconfig/migrations/
rm -rf order/migrations/

python manage.py makemigrations authentication
python manage.py migrate authentication

python manage.py makemigrations product
python manage.py migrate product

python manage.py makemigrations emailconfig
python manage.py migrate emailconfig

python manage.py makemigrations order
python manage.py migrate order

python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

python manage.py createsuperuser