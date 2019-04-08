class Credentials:
    credentials_list = []
    def __init__(self, account_name, account_user_name, account_password):
        self
    def add.credentials(self):
        Credentials.credentials_list.append(self)

    @classmethod
    def delete_credentials(cls, name):
        for account in 