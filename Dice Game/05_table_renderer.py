from tabulate import tabulate

class TableRenderer:
    def render_table(self, probabilities, dice):
        headers = ['User \\ Opponent'] + [','.join(map(str, die.values)) for die in dice]
        rows = []
        for i, row in enumerate(probabilities):
            row_data = [','.join(map(str, dice[i].values))] + row
            rows.append(row_data)
        return tabulate(rows, headers, tablefmt="grid")  # Return formatted table