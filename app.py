from flask import Flask, request, render_template






app = Flask(__name__)





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == "POST":
        return "hello man"


if __name__ == '__main__':
    app.run()
