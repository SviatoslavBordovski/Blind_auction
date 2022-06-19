from replit import clear
from view.cli_art import logo


# First solution

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


# Second solution

from replit import clear
from art import logo

def auction():
  print(logo)
  audience = {}

  bidders = True
  while bidders:

    # Tell name and bid, update a dictionary with received user's inputs
    name = input("Tell us your name?\n")
    bid_price = int(input("What is your bid?\n"))
    audience.update({name: bid_price})

    bidder = input("Is there someone else who would like to bid?\n").lower()
    clear()

    # If no bidders => stop loop and compare bids in dictionary choosing max key in it
    if bidder == 'no':
      bidders = False
      highest_made_bid(audience)

def highest_made_bid(bidders_dict):
  highest_bid = 0
  winner = ""
  for bidding_person in bidders_dict:
    bid_amount = bidders_dict[bidding_person]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidding_person
  print(f"Highest bid for now is {highest_bid}, so winner is {winner}!")
  
auction()
