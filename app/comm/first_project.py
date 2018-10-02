from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/admin')
def hello_admin():
    return '哈哈哈哈哈!'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
