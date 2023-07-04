# primeiro fazer a importação do flask
from flask import Flask, render_template, request

# apos nomear a apclicação é definido o parametro da aplicação
app = Flask(__name__)
frutas = []
# agora é criado uma rota
@app.route('/', methods=["GET", "POST", "DELETE"])
def principal():
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas)

@app.route('/sobre')
def sobre():
    notas = {"Lucas": 9.0, "Lorena": 8.0, "Fatima": 10.0, "leoncio": 10.0} 
    return render_template("sobre.html", notas=notas)