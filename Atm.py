print("\n\t\t\t\t****Insert Your Card****\n")
class Bank:
    def __init__(self,name,account_number,pin):
        self.name = name
        self.account_num = account_number
        self.pin = pin
        self.balance = 9000.00

    def account_details(self):
        print(f"ACCOUNT HOLDER NAME:\t{self.name}\nACCOUNT NUMBER:\t\tXXXX XXXX XXXX {self.account_num[-4:]}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"{amount}/- Amount Is Credited To Your Bank Account and Your Current Balance is {self.balance}/-")

    def withdrawal(self,amount1):
        if self.balance == 0 or amount1 > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amount1
            print(f"{amount1}/- Amount Is Debited And your Current Balance is {self.balance}/-")

    def check_balance(self):
        print(f"Your Current Balance is {self.balance}/-")
        
def while_if():
    print("\n1.Account Details\n2.Deposit\n3.Withdraw\n4.Balance\n")
    def first(_here):
            if _here == 1:
                s.account_details()
                hello()
            elif _here == 2:
                move = 1
                while(move):
                    amount = float(input("Place The Cash (only 100/200/500) to Deposit:"))
                    print("\n")
                    if(amount % 100 == 0 or amount % 200 == 0 or amount % 500 == 0):
                        s.deposit(amount)
                        hello()
                        move = 0
            
            elif _here == 3:
                move = 1
                while(move):
                    amount = float(input("Enter The Cash to be Withdrawal \n(Only Divisble of 100/200/500):"))
                    print("\n")
                    if(amount % 100 == 0 or amount % 200 == 0 or amount % 500 == 0):
                        s.withdrawal(amount)
                        hello()
                        move = 0
                
            elif _here == 4:
                s.check_balance()
                hello()
            else:
                print("Click The Number Between '0 to 4'")
                first(_here=int(input("Please Select The Form of Mode:")))
                print("\n")

    here = int(input("Please Select The Form of Mode Do You Want:"))
    print("\n")
    first(here)

def hello():
    ho = input("\nYou Want To Continue Press '0' or Press Any Key To Exit:")
    if ho == '0':
        while_if()
    else:
        print("\n\t\t\t*** Thank you For Using our ATM ***\n")


class Artist(Bank):
    def art_1(self,name,account_number,pin):
        Bank.__init__(self,name,account_number,pin)

    def art_2(self):
        count = 2
        while count >= 0:
            n = int(input("Enter Your PIN Number:"))
            if n == self.pin:
                while_if()
                break
            elif count == 0:
                print("Sorry,Please contact Your Bank.Your Card as been Locked")
                break
            elif n != self.pin:
                print(f"Please Enter Your Correct PIN Number.You Have {count} chance\n")
                count = count - 1

s = Artist("MR.VIJAY","4561 2340 8712 1509",4321)
s.art_2()


