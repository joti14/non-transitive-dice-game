from dice import Dice

class DiceParser:
    def parse_dice(self, args):
        dice = []
        for arg in args:
            values = arg.split(',')  # Split the input string by commas
            if len(values) != 6 or not all(v.isdigit() for v in values):
                raise ValueError(f"Invalid dice: {arg}")  # Raise an error if invalid
            dice.append(Dice([int(v) for v in values]))  # Create a Dice object
        if len(dice) < 3:
            raise ValueError("At least 3 dice are required.")  # Ensure at least 3 dice
        return dice 