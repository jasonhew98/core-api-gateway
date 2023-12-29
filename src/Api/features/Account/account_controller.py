from flask import Blueprint, jsonify
from account import AccountHandler
from infrastructure.services.core_service import CoreService

account_controller = Blueprint('account', __name__)
core_service = CoreService(base_url='http://external-service/api')
account_handler = AccountHandler(core_service)

@account_controller.route('/account', methods=['GET'])
def get_accounts():
    result = account_handler.get_accounts()
    return jsonify(result)
