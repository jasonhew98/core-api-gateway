from flask import Blueprint, jsonify
from .product import ProductHandler
from infrastructure.services.core_service import CoreService

product_controller = Blueprint('product', __name__)
core_service = CoreService(base_url='http://external-service/api')
product_handler = ProductHandler(core_service)

@product_controller.route('/product', methods=['GET'])
def get_products():
    result = product_handler.get_products()
    return jsonify(result)
