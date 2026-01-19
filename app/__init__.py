import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    template_path = os.path.join(base_dir, "templates")
    static_path = os.path.join(base_dir, "static")

    app = Flask(__name__, template_folder=template_path, static_folder=static_path)

    app.config.from_object("config.Config")

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
