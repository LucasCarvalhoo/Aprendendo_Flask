# primeiro fazer a importação do flask
from flask import Flask, render_template

# apos nomear a apclicação é definido o parametro da aplicação
app = Flask(__name__)

# agora é criado uma rota
@app.route('/')
def principal():
    notas = {"Lucas": 9.0, "Lorena": 8.0, "Fatima": 10.0, "leoncio": 10.0} 
    return render_template("index.html", notas=notas)

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")