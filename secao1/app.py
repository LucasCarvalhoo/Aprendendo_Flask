# primeiro fazer a importação do flask
from flask import Flask, render_template, request

# apos nomear a apclicação é definido o parametro da aplicação
app = Flask(__name__)
frutas = []
registros = []
# agora é criado uma rota
@app.route('/', methods=["GET", "POST", "DELETE"])
def principal():
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas)

@app.route('/sobre', methods = ["GET", "POST"])
def sobre():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
    return render_template("sobre.html", registros=registros)