import flask
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def get_message():
    print(request.json)

    return "yes"


if __name__ == '__main__':
    app.run(port=8003)