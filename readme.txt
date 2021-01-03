■redmineへ時間を登録するスクリプト
　参考URL：https://qiita.com/mima_ita/items/1a939db423d8ee295c85

■環境
　OS：Windows10 64bit
　python Ver.　python-3.9.1-amd64.exe

■設定
1.pythonをインストールする
　※動いたpython-3.9.1-amd64.exe
　※インストール時にパスを通す

2.コマンドプロンプトでパッケージをインストール
pip install python-redmine

3.redmine.pyの定義を変更する
8行目と9行目と10行目

4.ブラウザでredmineにログインして任意のチケットIDを確認

5.コマンドプロンプトでticketk_kakunin.pyを実行する
python ticketk_kakunin.py [チケットID]

6.上記を参考にredmine.pyを編集
22行目

■チケットを取得
1.redmine.pyをダブルクリック
2.csvファイルが作成される

■redmineに時間を登録
1.作成されたcsvファイルを編集する
2.編集したcsvファイルをredmine.pyにドラッグ&ドロップ


