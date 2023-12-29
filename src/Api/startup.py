import sys
sys.dont_write_bytecode = True

from flask import Flask
from features.Chat.chat_controller import chat_controller
from features.Account.account_controller import account_controller
from features.Product.product_controller import product_controller
from appsettings import Configuration

app = Flask(__name__)

app.config.from_object(Configuration(environment='development' if app.debug else 'production'))

# Register blueprints
app.register_blueprint(chat_controller, url_prefix='/api')
app.register_blueprint(account_controller, url_prefix='/api')
app.register_blueprint(product_controller, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
