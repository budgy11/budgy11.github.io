#7.3
#CS 1030 - Victor Semenok
#6:00 PM TR Fall 2017
#Create a bank account
#
class Account:
    def __init__(self, id = 0, balance = 100.00, annualInterestRate = 0):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate
    def setid(self, id):
        self.id = id
    def setbalance(self, balace):
        self.balance = balance
    def setannualInterestRate(self,annualInterestRate):
        self.annualInterestRate = annualInterestRate
    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12
    def getMonthlyInterest(self):
        return (((self.annualInterestRate / 100) / 12) + 1) * self.balance
    def withdraw(self, amt):
        self.balance = self.balance - amt
        return self.balance
    def deposit(self, Damt):
        self.balance = self.balance + Damt
        return self.balance
