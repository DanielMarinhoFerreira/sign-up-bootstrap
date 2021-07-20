from app import criar_app


app = criar_app() # guarda uma função do arvivo __init__.py


if __name__ == '__main__': # verifica a inicialização 
    app.run(debug=True) # inicializar