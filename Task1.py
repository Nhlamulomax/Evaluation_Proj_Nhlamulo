from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello MDM, I am testing some libraries"

if __name__ == "__main__":
    app.run()
