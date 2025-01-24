import random

class Dice:
    def __init__(self, values):
        self.values = values  # Store the values of the die

    def roll(self):
        return random.choice(self.values)  # Roll the die and return a random value