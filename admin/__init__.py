from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel, Domain


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# Initialize babel
babel = Babel(app, default_domain=Domain())

SUPPORTED_LANGUAGES = ['en', 'zh_CN', 'zh_TW']

@babel.localeselector
def get_locale():
    accept_language = request.accept_languages.best_match(SUPPORTED_LANGUAGES)
    override = request.args.get('lang')
    if override:
        session['lang'] = override

    return session.get('lang', accept_language)



import admin.main
