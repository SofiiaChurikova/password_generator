from flask import Flask, render_template, url_for, request
import secrets
import string

app = Flask(__name__)
def to_generate(lett_num, symb_num, numb_num):
    letters = ''.join(secrets.choice(string.ascii_letters) for _ in range(lett_num))
    symbols = ''.join(secrets.choice(string.punctuation) for _ in range(symb_num))
    numb_num = ''.join(secrets.choice(string.digits) for _ in range(numb_num))
    password = list(letters + symbols + numb_num)
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)
@app.route('/', methods=["GET", "POST"])

def password():
    generatedPass = None
    if request.method == "POST":
        letters_num = int(request.form.get("letters", 0))
        symbols_num = int(request.form.get("symbols", 0))
        numbers_num = int(request.form.get("numbers", 0))
        generatedPass = to_generate(letters_num,symbols_num,numbers_num)
        return render_template('index.html', password=generatedPass)
    return render_template("index.html", password=None)
if __name__ == "__main__":
    app.run(debug=True)