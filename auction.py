from replit import clear
from view.cli_art import logo

def auction():
  print(logo)
  audience = {}

  bidders = True
  while bidders:

    # Ask user his/her name and preferred bid, update a dictionary with received user's inputs
    name = input("Tell us your name?\n")
    bid_price = int(input("What is your bid?\n"))
    audience.update({name: bid_price})
    
    bidder = input("Is there someone else who would like to bid?\n").lower()
    clear()

    # If there are no bidders => stop loop and compare bids in dictionary choosing maximum key in it
    if bidder == 'no':
      bidders = False
      highest_bid_name = max(audience, key=audience.get)
      print(f'Highest bid made {highest_bid_name}, congrats!')

auction()
