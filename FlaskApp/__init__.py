from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello This server was setup in less than 10 mintues :)'

if __name__ == "__main__":
        app.run(Debug=True)
