git clone git@github.com:mijiturka/flask-uwsgi-nginx.git
git pull

cp ../server/main.py flask-uwsgi-nginx/server/app
cp ../server/requirements.txt flask-uwsgi-nginx/server/app

cp -r ../client/* flask-uwsgi-nginx/server/static
