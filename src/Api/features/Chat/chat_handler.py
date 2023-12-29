class ChatHandler:
    def __init__(self, open_ai_service):
        self.open_ai_service = open_ai_service

    def get_chat_completion(self):
        response = self.open_ai_service.get_chat_completion()
        return response.choices[0].message.content
