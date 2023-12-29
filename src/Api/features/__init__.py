from flask import Flask
from features.Account.account_controller import account_controller
from features.Product.product_controller import product_controller

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(account_controller, url_prefix='/api')
    app.register_blueprint(product_controller, url_prefix='/api')

    return app
