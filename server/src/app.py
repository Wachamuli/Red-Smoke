from flask import Flask
from flask_cors import CORS


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(f"config.{config}")

    CORS(app)

    return app
