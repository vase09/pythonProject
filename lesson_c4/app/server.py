from flask import Flask

from lesson_c4.app.views import start_bp, fight_bp


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    # Register blueprints
    app.register_blueprint(start_bp)
    app.register_blueprint(fight_bp)

    return app
