class Bankz_Account():

    def __init__(self, name, balan, user_name, user_balan):
        self.name = name   
        self.balan = balan

        self.user_name = user_name   
        self.user_balan = user_balan

    def cash_depoz(self, cash_deposit):
        self.balan = self.balan + cash_deposit
    
    def cash_withdraw(self, cash_withdraw):
        self.balan = self.balan - cash_withdraw

    def cash_transfer(self, cash_transfer):
        self.balan = self.balan - cash_transfer
        cash_transfer + self.user_balan

    def display_balan(self):
        print(self.name, 'has', self.balan)

bimis_acc = Bankz_Account("Bimi", 39280)
user_acc = Bankz_Account("User", 35003)

user_acc.display_balan()
user_acc.cash_depoz(23000)
user_acc.display_balan()
user_acc.cash_withdraw(1)
user_acc.cash_transfer(1)
user_acc.display_balan()

bimis_acc.display_balan()
bimis_acc.cash_depoz(23000)
bimis_acc.display_balan()
bimis_acc.cash_withdraw(1)
bimis_acc.cash_transfer(1)
bimis_acc.display_balan()