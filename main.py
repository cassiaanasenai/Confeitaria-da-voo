from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicial():
    return render_template("index.html")

@app.route("/contatos")
def contato():
    return render_template("contato.html")


if __name__ == '__main__':
    app.run()