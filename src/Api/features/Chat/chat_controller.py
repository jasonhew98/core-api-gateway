from flask import Blueprint, jsonify
from infrastructure.services.open_ai_service import OpenAIService
from .chat_handler import ChatHandler

open_ai_service = OpenAIService()

chat_controller = Blueprint('chat', __name__)
chat_handler = ChatHandler(open_ai_service)

@chat_controller.route('/chat', methods=['GET'])
def get_chat_completion():
    result = chat_handler.get_chat_completion()
    return jsonify(result)
