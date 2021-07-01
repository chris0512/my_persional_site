from flask import Flask

# run application in current directory:__name__
app = Flask(__name__)


# app decorator to target home route
@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)