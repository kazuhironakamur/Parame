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

# アプリケーションの作成
python manage.py startapp <app>
