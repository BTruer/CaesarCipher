from flask import Flask, request, render_template
from logic import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    textE = ""
    textD = ""
    if request.method == 'GET':
        return render_template("index.html", textE=textE, textD=textD)
    if request.method == "POST":
        if(request.form.get('submitButton') == "encryptMe"):
            plaintext = request.form.get('plaintext')
            keyE = request.form.get('keyE')
            textE = getCiphertext(keyE,plaintext)
            return render_template("index.html", textE=textE, textD=textD)
        elif(request.form.get('submitButton') == "decryptMe"):
            ciphertext = request.form.get('ciphertext')
            keyD = request.form.get('keyD')
            textD = getPlaintext(keyD,ciphertext)
            return render_template("index.html", textE=textE, textD=textD)
        elif(request.form.get('submitButton') == "attackMe"):
            ciphertext = request.form.get('ciphertext')
            textD = getPlaintextAll(ciphertext)
            return render_template("index.html", textE=textE, textD=textD)

if __name__ == '__main__':
    app.run(debug=True)
