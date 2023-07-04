# primeiro fazer a importação do flask
from flask import Flask, render_template

# apos nomear a apclicação é definido o parametro da aplicação
app = Flask(__name__)

# agora é criado uma rota
@app.route('/')
def principal():
    fruta1 = "morango"
    fruta2 = "uva"
    fruta3 = "maçã"
    fruta4 = "laranja"
    return render_template("index.html", 
                            fruta1=fruta1,
                            fruta2=fruta2,
                            fruta3=fruta3,
                            fruta4=fruta4)

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")