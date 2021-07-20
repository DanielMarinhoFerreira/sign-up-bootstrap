from flask import Flask


def criar_app(): # função que tem as configuração do app 
    
    app = Flask (__name__)
    app.config['SECRET_KEY'] = 'FNSKDAHFKFDDLNFDNLJ'
    
    from .views import views # importa as views para dentro da função 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app 