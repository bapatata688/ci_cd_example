from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return {
        "mensaje": "API de ventas operativa"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
