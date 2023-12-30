class UserHandler:
    def __init__(self, core_service):
        self.core_service = core_service

    def get_user(self):
        user = self.core_service.get_user()
        return user
