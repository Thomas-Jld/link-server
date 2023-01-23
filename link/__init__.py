import os
from flask import Flask, request
from flask_cors import CORS

APP_NAME = "link"

def create_app(test_config=None, do_init_db=False):
    app = Flask(__name__,  static_url_path="/link/static", instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "link.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    CORS(app)

    from link.db import init_app, init_db
    init_app(app)
    if do_init_db or not os.path.exists(app.config["DATABASE"]):
        with app.app_context():
            init_db()

    from link.register import register_bp
    app.register_blueprint(register_bp)

    from link.update import update_bp
    app.register_blueprint(update_bp)

    from link.stats import stats_bp
    app.register_blueprint(stats_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run("0.0.0.0", port=27151)
