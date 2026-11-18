from pathlib import Path
from flask import Flask
from config import Config
from .extensions import db, migrate


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    # Read at factory time, after run.py has loaded environment variables.
    import os
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    if test_config:
        app.config.update(test_config)
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    from .routes.main import bp
    app.register_blueprint(bp)
    return app
