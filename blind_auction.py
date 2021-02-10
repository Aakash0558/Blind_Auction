from replit import clear
from art import logo

print(logo)

bid_again = True

auction_records = {}

while bid_again:
  name = input("Please enter your name:\n").lower()
  bid = int(input("Please enter your bid:\n$"))

  auction_records[name] = bid

  other_bidders = input("Are there other users who want to bid? type 'yes' or 'no'.\n").lower()

  if other_bidders == "yes":
    bid_again = True
    clear()
  elif other_bidders == "no":
    bid_again = False
  else:
    print("Wrong input! Type 'yes' or 'no' again.") 
  
winner_name = ''
winning_bid = 0

for names in auction_records:
  if winning_bid < auction_records[names]:
    winning_bid = auction_records[names]
    winner_name = names
    clear()
  
print(f"The winner is {winner_name} with a bid of ${winning_bid}.")
