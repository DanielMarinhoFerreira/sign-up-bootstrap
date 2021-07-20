from flask import Blueprint
from flask import render_template


views = Blueprint('views', __name__)


# retorna Barra inicial do html "UTILIZAR PARA TESTE O VIEWS" 
@views.route('base')
def base ():
    return render_template ("base.html")


# visualização "padrão" inicial quando a padina é aberta
@views.route('/')
def page ():
    return render_template("home.html")


# teste para o Login que está em "auth"
#@views.route('Login')
#def login ():
    return render_template("login.html")


# teste de conteuno inicial pata o site
@views.route('Teste')
def teste():
    return render_template("teste.html")
