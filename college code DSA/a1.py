class Bank_Account:
  def __init__(self):
    self.balance=0
    print("\nHello!!! Welcome to the Deposit & Withdrawal Machine\n")

  def deposit(self):
    amount=float(input("Enter amount to be Deposited: "))
    self.balance += amount
    print("\n Amount Deposited:",amount)

  def withdraw(self):
    amount = float(input("Enter amount to be Withdrawn: "))
    if self.balance>=amount:
      self.balance-=amount
      print("\n You Withdrew:", amount)
    else:
      print("\n Insufficient balance ")

  def display(self):
    print("\n Net Available Balance=",self.balance)

s = Bank_Account()
while True:
    print("1.Deposite")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit\n")
    ch=int(input("Enter your choice : "))
    if(ch==1):
        s.deposit()
    elif(ch==2):
        s.withdraw()
    elif(ch==3):
        s.display()
    if(ch==4):
        break
