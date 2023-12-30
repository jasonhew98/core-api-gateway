class ProductHandler:
    def __init__(self, core_service):
        self.core_service = core_service

    def get_products(self):
        products = self.core_service.get_products()
        return products
