from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")  # <-- here
    app.config.from_object("config.Config")

    db.init_app(app)

    # Import and register your routes
    from .routes import main
    app.register_blueprint(main)

    return app
