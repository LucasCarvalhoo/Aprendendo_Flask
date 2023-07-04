# primeiro fazer a importação do flask
from flask import Flask, render_template

# apos nomear a apclicação é definido o parametro da aplicação
app = Flask(__name__)

# agora é criado uma rota
@app.route('/')
def principal():
    frutas = ["Morango", "Maçã", "Uva", "Laranja"]
    return render_template("index.html", frutas=frutas)

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")