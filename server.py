from flask import Flask, render_template

# run application in current directory:__name__
app = Flask(__name__)


# app decorator to target home route
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
