# class Credentials:
#     credentials_list = []
#     def __init__(self, account_name, account_user_name, account_password):
#         self
#     def add.credentials(self):
#         Credentials.credentials_list.append(self)

#     @classmethod
#     def delete_credentials(cls, name):
#         for account in 
class Credentials:
    """
    Class that generates new instances of user application credentials
    """

    credentials_list = []

    def __init__(self, account_name, account_user_name, account_password):
        '''
        __init__ method that defines properties for our credentials objects.
        '''

        self.account_name = account_name
        self.account_user_name = account_user_name
        self.account_password = account_password

    def add_credentials(self):
        '''
        add_credentials method adds a new account's credentials object into credentials_list
        '''

        Credentials.credentials_list.append(self)

    @classmethod
    def delete_credentials(cls, name):
        '''
        delete_credentials method deletes an account's saved credentials from the credentials_list
        '''

        for account in cls.credentials_list:
            if account.account_name == name:
                Credentials.credentials_list.remove(account)

    @classmethod
    def display_all_accounts(cls):
        '''
        display_all_accounts method returns the credentials list
        '''

        return cls.credentials_list

    @classmethod
    def find_by_account(cls, name):
        '''
        find_by_account method takes a searched account name and returns account credentials of that account.

        Args:
            account: Account name to search for
        Returns :
            Credentials of the user account that matches the searched account.
        '''

        for account in cls.credentials_list:
            if account.account_name == name:
                return account