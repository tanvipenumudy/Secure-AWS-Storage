from flask import Flask, render_template, request, redirect, url_for, flash, \
    Response, session, Blueprint, send_file, make_response, jsonify
from flask_bootstrap import Bootstrap
from filters import datetimeformat, file_type
from flask_login import login_required, current_user
# from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from resources import get_bucket, get_buckets_list

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'secret-key'
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type

db = SQLAlchemy()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
        return render_template("profile.html", name=current_user.name)

@app.route('/bucket', methods=['GET', 'POST'])
@login_required
def bucket():
    if request.method == 'POST':
        bucket = request.form['bucket']
        session['bucket'] = bucket
        return redirect(url_for('files'))
    else:
        buckets = get_buckets_list()
    return render_template("bucket.html", buckets=buckets)


@app.route('/files')
@login_required
def files():
    my_bucket = get_bucket()
    summaries = my_bucket.objects.all()

    return render_template('files.html', my_bucket=my_bucket, files=summaries)

def create_app():

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    app_blueprint = Blueprint('app', __name__)
    app.register_blueprint(app_blueprint)
    return app

def run_app():
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.get(int(user_id))
    app.run(debug=True)

if __name__ == "__main__":
    run_app()
