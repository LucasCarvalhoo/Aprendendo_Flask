# primeiro fazer a importação do flask
from flask import Flask

# apos nomear a apclicação é definido o parametro da aplicação
app = Flask(__name__)

# agora é criado uma rota
@app.route('/')
def principal():
    return 'Hello world'