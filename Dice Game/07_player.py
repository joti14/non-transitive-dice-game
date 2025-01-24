class Player:
    def __init__(self, name):
        self.name = name  # Store the player's name
        self.dice = None  # Initialize the dice attribute

    def choose_dice(self, dice_options):
        print("Available dice:")
        for i, die in enumerate(dice_options):
            print(f"{i}: {die.values}")  # Display available dice
        choice = int(input("Select a die by number: "))  # Get user's choice
        self.dice = dice_options[choice]  # Set the chosen die