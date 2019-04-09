# ファイルからのpip install
pip install -r requirements.txt

# Profileの読み込み
cd C:\django\web

..\wakoit\Scripts\activate

# 開発用Webサーバー起動
python manage.py runserver

# 管理者ユーザーの作成
python manage.py createsuperuser

# DBのmigrate
python manage.py migrate

# modelをもとにmigrationを作成
python manage.py makemigrations blog

# 続いてmigrate
python manage.py migrate blog

# アプリケーションの作成
python manage.py startapp <app>

# django shell
from parame.models import Project
Project.objects.all()

# pythonanywhereへのデプロイ
pa_autoconfigure_django.py https://github.com/kazuhironakamur/taby-django.git

# pythonanywhereへの再デプロイ
pa_autoconfigure_django.py --nuke https://github.com/kazuhironakamur/taby-django.git

#admin
id: wakoit
pw: django!

#pythonのバージョンを3.6に変更
python 3.6をインストールしてから以下を実行
virtualenv -p "C:\Users\nakamura_k\AppData\Local\Programs\Python\Python36-32\python.exe" taby_env

# Windows環境でpostgresに接続
psql --username=postgres
pass: goyounaraba

# heroku
git push heroku master
heroku ps:scale web=1
heroku open
heroku logs --tail

heroku run python manage.py migrate
heroku run python manage.py createsuperuser