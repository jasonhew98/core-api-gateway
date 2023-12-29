import requests

class OpenAIService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_chat_completion(self):
        endpoint_url = f"{self.base_url}/chat"
        response = requests.get(endpoint_url)
        return response.json()
