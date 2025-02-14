import random as r

# Read and process odds data from a file
odds_details = []
with open('odds.txt', mode='r') as f:
    odds_details = f.readlines()

# Remove comment lines from the odds data
odds_details = [i for i in odds_details if i[0] != '#']

# Set the number of games to analyze
num_of_games = 20
odds_details = odds_details[:num_of_games]

# Extract actual game outcomes from the odds data
outcomes = []
for i in odds_details:
    outcomes.append(i.split()[6])

# Extract betting odds for home win (1), draw (X), and away win (2)
odds_details_split = []
for i in odds_details:
    odds_details_split.append([float(i.split()[2]), float(i.split()[3]), float(i.split()[4])])

# Generate weighted choices based on the odds for each game
genChoices = []
for i in odds_details:
    genChoices.append(
        ['1' for _ in range(int(float(i.split()[2]) * 100))] +
        ['X' for _ in range(int(float(i.split()[3]) * 100))] +
        ['2' for _ in range(int(float(i.split()[4]) * 100))]
    )

# Generate 20 sets of random predictions based on the weighted odds
all_choices = []
for i in range(20):
    choices = []
    for j in genChoices:
        choices.append(r.choice(j))  # Randomly select an outcome
    all_choices.append(choices)

# Function to compare actual outcomes with generated predictions
def compare(outcome, predictions):
    compare_list = []
    for i in predictions:
        amount = 0
        for j in range(len(i)):
            if i[j] == outcome[j]:  # Check if prediction matches actual outcome
                if outcome[j] == '1':
                    amount += odds_details_split[j][0] * 100  # Home win payout
                elif outcome[j] == '2':
                    amount += odds_details_split[j][2] * 100  # Away win payout
                else:
                    amount += odds_details_split[j][1] * 100  # Draw payout
        compare_list.append(amount)  # Store total earnings per prediction set
    return compare_list

# Compare generated predictions against actual results
comp_list = compare(outcomes, all_choices)

# Print results: individual earnings, total earnings, and average earnings per prediction set
print(comp_list)
print(sum(comp_list), num_of_games * 100 * 20)
print(sum(comp_list) / len(comp_list))