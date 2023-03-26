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

    def accounts_by_customer(self, customer_id):
        accounts = []
        for account in self._accounts.values():
            if account.get_customer_id() == customer_id:
                accounts.append(account)
        return accounts

    def remove_account(self, account_nbr):
        account = self._accounts.get(account_nbr)
        if account is not None and account.get_balance() == 0:
            del self._accounts[account_nbr]
            return True
        else:
            return False

    def transfer(self, from_account_nbr, to_account_nbr, amount):
        from_account = self._accounts.get(from_account_nbr)
        to_account = self._accounts.get(to_account_nbr)
        if from_account is None or to_account is None:
            return False
        elif from_account.get_balance() < amount:
            return False
        else:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            return True

    def total_balances(self):
        return sum(account.get_balance() for account in self._accounts.values())

    def all_accounts(self):
        return list(self._accounts.values())

    def all_accounts_sorted_by_balance(self):
        accounts_list = list(self._accounts.values())

        for i in range(len(accounts_list)):
            max_idx = i
            for j in range(i+1, len(accounts_list)):
                if accounts_list[j].get_balance() > accounts_list[max_idx].get_balance():
                    max_idx = j
            accounts_list[i], accounts_list[max_idx] = accounts_list[max_idx], accounts_list[i]

        return accounts_list
    

    
    
print('=====================================================')
bank = Bank()

bank.add_customer('Fredrik')
bank.create_account('C1')
bank.create_account('C1')
bank.create_account('C1')

account1 = bank.get_account(1)
account2 = bank.get_account(2)
account3 = bank.get_account(3)

if account1:
    account1.deposit(100)
if account2:
    account3.deposit(1000)
if account3:
    account1.deposit(500)


print(f"all accounts: {bank.all_accounts()}")

print(f"Sorted accounts: {bank.all_accounts_sorted_by_balance()}")

