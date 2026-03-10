from flask import Flask
from .views.routes import api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api) # 将蓝图注册到应用中
    return app