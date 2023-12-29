class ProductHandler:
    def __init__(self, core_service):
        self.core_service = core_service

    def get_products(self):
        accounts = self.core_service.get_products()
        return {'accounts': accounts, 'data_from_external_service': accounts}
