from flask import *  # 必要なライブラリのインポート

app = Flask(__name__)  # アプリの設定


@app.route("/")  # どのページで実行する関数か設定
def main():
    return render_template('index.html',text="わたしテキスト",page_title="お試しページ")
    #最初に読み込むhtmlと、htmlに渡す変数を指定

@app.route("/json")  # どのページで実行する関数か設定
def static_file():
    return send_file('myexperiment/abc.json')
    #最初に読み込むhtmlと、htmlに渡す変数を指

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8888 で スレッドオンで実行