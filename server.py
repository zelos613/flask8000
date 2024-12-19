from flask import Flask

# Flaskアプリケーションの作成
app = Flask(__name__)

# ヘルスチェック用のエンドポイント
@app.route("/")
def health_check():
    return "OK", 200

# アプリケーションの実行
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
