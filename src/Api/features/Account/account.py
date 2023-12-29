class AccountHandler:
    def __init__(self, core_service):
        self.core_service = core_service

    def get_accounts(self):
        accounts = self.core_service.get_accounts()
        return {'accounts': accounts, 'data_from_external_service': accounts}
