# random is a library that allows us to generate random numbers and make random choices.
import random

low = 1
high = 100
cards = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
choices = ("rock", "paper", "scissors")


# Generate a random integer between low and high (inclusive)
random_number = random.randint(low, high)
print(f"Random number between {low} and {high}: {random_number}")

# Make a random choice from the choices tuple
random_choice = random.choice(choices)
print(f"Random choice from {choices}: {random_choice}")

# Shuffle the cards list
random.shuffle(cards)
print(f"Shuffled cards: {cards}")

# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")




