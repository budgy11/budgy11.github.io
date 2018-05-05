from BankAccount import Account
def main():
    Account1 = Account(1122, 20000, 4.5)
    Account1.withdraw(2500)
    Account1.deposit(3000)
    print("The Account id is", Account1.id)
    print("The current account balance stands at", round(Account1.balance, 2))
    print("The monthly interest rate on the account is", Account1.getMonthlyInterestRate(),"percent")
    print("The projected balance at the end of the month is", round(Account1.getMonthlyInterest(), 2))
main()
