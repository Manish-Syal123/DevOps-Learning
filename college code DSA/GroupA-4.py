# Initialize the balance to 0
balance = 0

def deposit(amount):
  # Increase the balance by the given amount
  global balance
  balance += amount

def withdraw(amount):
  # Decrease the balance by the given amount if the balance is not going negative
  global balance
  if balance - amount >= 0:
    balance -= amount
  else:
    print("Error: Withdrawal is not allowed if balance is going negative")

# Read the transaction log from the console input
transaction_log = input("Enter the transaction log: ")

# Split the transaction log into a list of transactions
transactions = transaction_log.split(", ")

# Iterate through the list of transactions
for transaction in transactions:
  # Split the transaction into the transaction type and amount
  transaction_type, amount = transaction.split()
  amount = int(amount)
  
  # Perform the appropriate action based on the transaction type
  if transaction_type == "D":
    deposit(amount)
  elif transaction_type == "W":
    withdraw(amount)

# Print the final balance
print("The final balance is:", balance)
