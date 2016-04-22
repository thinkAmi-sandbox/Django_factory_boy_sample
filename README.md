# Django_factory_boy_sample


## セットアップ
```
# 任意のGit用ディレクトリへ移動
>cd path\to\dir

# GitHubからカレントディレクトリへclone
path\to\dir>git clone https://github.com/thinkAmi-sandbox/Django_factory_boy_sample.git

# virtualenv環境の作成とactivate
# *Python3.5は、`c:\python35-32\`の下にインストール
path\to\dir>virtualenv -p c:\python35-32\python.exe env
path\to\dir>env\Scripts\activate

# requirements.txtよりインストール
(env)path\to\dir>pip install -r requirements.txt

# 実行(-sオプションで、print()の結果も表示)
(env)path\to\dir>py.test -s
```

　  
## テスト環境

- Windows10
- Python 3.5.1
- Django 1.9.5
- pytest 2.9.1
- pytest-django 2.9.1
- factory-boy 2.7.0

　  
## 関係するブログ
[Django + factory_boyで、1対多や多対多のリレーションを持つテストデータを作る - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/04/22/233958)