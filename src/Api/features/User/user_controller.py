from flask import Blueprint, jsonify
from .user_handler import UserHandler
from infrastructure.services.core_service import CoreService

user_controller = Blueprint('user', __name__)
core_service = CoreService(base_url='http://external-service/api')
user_handler = UserHandler(core_service)

@user_controller.route('/user', methods=['GET'])
def get_user():
    result = user_handler.get_user()
    return jsonify(result)
