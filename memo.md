# ファイルからのpip install
pip install -r requirements.txt

# Profileの読み込み
cd C:\django\web
..\wakoit\Scripts\activate

# 開発用Webサーバー起動
python manage.py runserver

# DBのmigrate
python manage.py migrate