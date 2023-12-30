import requests

class CoreService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_user(self):
        endpoint_url = f"{self.base_url}/account"
        response = requests.get(endpoint_url)
        return response.json()

    def get_products(self):
        endpoint_url = f"{self.base_url}/product"
        response = requests.get(endpoint_url)
        return response.json()
