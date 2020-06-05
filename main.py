from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
   return "Hello WORLD"


@app.route('/<name>')
def home_name(name):
   return "Hello {}".format(name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
