from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)


@auth.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('senha')

    return render_template("login.html")
        #user = User.query.filter_by(email=email).first()
