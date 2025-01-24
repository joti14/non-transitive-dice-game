from itertools import product

class ProbabilityCalculator:
    def calculate_probabilities(self, dice):
        n = len(dice)
        probabilities = [[0] * n for _ in range(n)]  # Create a matrix for probabilities
        for i in range(n):
            for j in range(n):
                if i != j:  # Only compare different dice
                    win_count = sum(a > b for a in dice[i].values for b in dice[j].values)
                    total_outcomes = len(dice[i].values) * len(dice[j].values)
                    probabilities[i][j] = win_count / total_outcomes  # Calculate probability
        return probabilities