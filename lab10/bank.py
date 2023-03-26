from account import Account

class Bank:
    def __init__(self):
        self._customers = {}
        self._accounts = {}
        self._next_customer_id = 1
        self._next_account_nbr = 1

    def add_customer(self, name):
        customer_id = 'C' + str(self._next_customer_id)
        self._customers[customer_id] = name
        self._next_customer_id += 1
        return customer_id

    def get_customer_name(self, customer_id):
        return self._customers.get(customer_id)

    def create_account(self, customer_id):
        if customer_id in self._customers:
            account_nbr = self._next_account_nbr
            self._accounts[account_nbr] = Account(customer_id, account_nbr)
            self._next_account_nbr += 1
            return account_nbr
        else:
            return -1

    def get_account(self, account_nbr):
        return self._accounts.get(account_nbr)