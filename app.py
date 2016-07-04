from flask import Flask, request, render_template
from logic import getCiphertext, getPlaintext

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    PostTrue = False
    textE = ""
    textD = ""
    if request.method == 'GET':
        return render_template("index.html", PostTrue=PostTrue, textE=textE, textD=textD)
    if request.method == "POST":
        if(request.form.get('submitButton') == "encryptMe"):
            plaintext = request.form.get('plaintext')
            keyE = request.form.get('keyE')
            textE = getCiphertext(keyE,plaintext)
            PostTrue = True
            return render_template("index.html", PostTrue=PostTrue, textE=textE, textD=textD)
        elif(request.form.get('submitButton') == "decryptMe"):
            ciphertext = request.form.get('ciphertext')
            keyD = request.form.get('keyD')
            textD = getPlaintext(keyD,ciphertext)
            return render_template("index.html", PostTrue=True, textE=textE, textD=textD)


if __name__ == '__main__':
    app.run(debug=True)
