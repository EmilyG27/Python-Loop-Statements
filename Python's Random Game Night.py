# Task 1
import random

players_guess = input("Do you think the card will be a King, Queen, or Ace? ")
cards = ["King", "Queen", "Ace"]

if players_guess == random.choice(cards):
    print("Correct!")
else:
    print("Try again")