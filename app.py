from flask import Flask, request, render_template
from logic import getCiphertext

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    encryptPost = None
    if request.method == 'GET':
        return render_template("index.html", encryptPost=encryptPost)
    if request.method == "POST":
        plaintext = request.form.get('plaintext')
        keyE = request.form.get('keyE')
        encryptPost = getCiphertext(keyE,plaintext)
        return render_template("index.html", encryptPost=encryptPost)



if __name__ == '__main__':
    app.run(debug=True)
