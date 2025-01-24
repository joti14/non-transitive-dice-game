import sys
from dice_parser import DiceParser
from random_generator import RandomGenerator
from probability_calculator import ProbabilityCalculator
from table_renderer import TableRenderer
from fairness_verifier import FairnessVerifier
from player import Player

class Game:
    def __init__(self):
        self.parser = DiceParser()  # Initialize the parser
        self.random_gen = RandomGenerator()  # Initialize the random generator
        self.prob_calc = ProbabilityCalculator()  # Initialize the probability calculator
        self.table_renderer = TableRenderer()  # Initialize the table renderer
        self.verifier = FairnessVerifier()  # Initialize the HMAC verifier
        self.players = [Player("Player 1"), Player("Computer")]  # Create players

    def start(self, args):
        try:
            dice = self.parser.parse_dice(args)  # Parse the dice configurations
            print("Game started with dice:", [d.values for d in dice])
            probabilities = self.prob_calc.calculate_probabilities(dice)  # Calculate probabilities
            print(self.table_renderer.render_table(probabilities, dice))  # Display the table

            # Determine who goes first
            key = self.random_gen.generate_secure_key()
            random_number, hmac_value = self.random_gen.generate_random_number(1, key)  # 0 or 1
            print(f"I selected a random value in the range 0..1 (HMAC={hmac_value}).")
            print("Try to guess my selection.")
            print("0 - 0")
            print("1 - 1")
            print("X - exit")
            print("? - help")

            user_input = input("Your selection: ")
            if user_input == '0':
                print("You go first!")
                first_player = self.players[0]
                second_player = self.players[1]
            elif user_input == '1':
                print("Computer goes first!")
                first_player = self.players[1]
                second_player = self.players[0]
            else:
                print("Exiting the game.")
                return

            # First player chooses their dice
            first_player.choose_dice(dice)
            print(f"{first_player.name} chose: {first_player.dice.values}")

            # Computer randomly selects its dice
            available_dice = [die for die in dice if die != first_player.dice]
            second_player.dice = random.choice(available_dice)
            print(f"{second_player.name} chose: {second_player.dice.values}")

            # Generate random number and HMAC for fairness
            key = self.random_gen.generate_secure_key()
            computer_random_number, computer_hmac_value = self.random_gen.generate_random_number(5, key)

            print(f"Computer generated random number: {computer_random_number}, HMAC: {computer_hmac_value}")

            # User makes a choice
            player_choice = int(input("Choose a number between 0 and 5: "))

            # Verify HMAC
            if self.verifier.verify_hmac(computer_random_number, key, computer_hmac_value):
                print("HMAC verified successfully.")
                
                # Calculate the result using modular addition
                result = (computer_random_number + player_choice) % 6
                print(f"Result of (computer number + player choice) % 6 = {result}")

                # Roll the dice
                player_roll = first_player.dice.roll()
                computer_roll = second_player.dice.roll()
                print(f"{first_player.name} rolled: {player_roll}")
                print(f"{second_player.name} rolled: {computer_roll}")

                # Determine the winner
                if player_roll > computer_roll:
                    print(f"{first_player.name} wins!")
                elif player_roll < computer_roll:
                    print(f"{second_player.name} wins!")
                else:
                    print("It's a tie!")
            else:
                print("HMAC verification failed. Possible tampering detected.")

        except ValueError as e:
            print("Error:", e)
            print("Usage: python dice.py <dice1> <dice2> <dice3> ...")

# Example usage
if __name__ == "__main__":
    game = Game()
    game.start(sys.argv[1:])