import random  # Importing the 'random' module to enable functionality for random number generation.
from dataclasses import dataclass  # Importing 'dataclass' to simplify the creation of classes for data management.


# The '@dataclass' decorator is used to simplify the creation of classes.
# It automatically generates special methods like __init__(), __repr__(), and __eq__()
# based on the attributes specified within the class.
@dataclass
class Team:
    # 'name' is a class attribute that will store the name of the team as a string.
    name: str

    # 'seed' is a class attribute that will store the seed/rank of the team as an integer.
    seed: int


# Define the first round matchups for the basketball tournament.

first_round = [
    # SOUTH REGION
    (Team("Auburn", seed=1), Team("Alabama St./Saint Francis U.", seed=16)),
    (Team("Louisville", seed=8), Team("Creighton", seed=9)),
    (Team("Michigan", seed=5), Team("UC San Diego", seed=12)),
    (Team("Texas A&M", seed=4), Team("Yale", seed=13)),
    (Team("Ole Miss", seed=6), Team("San Diego St./North Carolina", seed=11)),
    (Team("Iowa St.", seed=3), Team("Lipscomb", seed=14)),
    (Team("Marquette", seed=7), Team("New Mexico", seed=10)),
    (Team("Michigan St.", seed=2), Team("Bryant", seed=15)),

    # WEST REGION
    (Team("Florida", seed=1), Team("Norfolk St.", seed=16)),
    (Team("UConn", seed=8), Team("Oklahoma", seed=9)),
    (Team("Memphis", seed=5), Team("Colorado St.", seed=12)),
    (Team("Maryland", seed=4), Team("Grand Canyon", seed=13)),
    (Team("Missouri", seed=6), Team("Drake", seed=11)),
    (Team("Texas Tech", seed=3), Team("UNC Wilmington", seed=14)),
    (Team("Kansas", seed=7), Team("Arkansas", seed=10)),
    (Team("St. John's", seed=2), Team("Omaha", seed=15)),

    # EAST REGION
    (Team("Duke", seed=1), Team("America/Mount St. Mary's", seed=16)),
    (Team("Mississippi St.", seed=8), Team("Baylor", seed=9)),
    (Team("Oregon", seed=5), Team("Liberty", seed=12)),
    (Team("Arizona", seed=4), Team("Akron", seed=13)),
    (Team("BYU", seed=6), Team("VCU", seed=11)),
    (Team("Wisconsin", seed=3), Team("Montana", seed=14)),
    (Team("Saint Mary's", seed=7), Team("Vanderbilt", seed=10)),
    (Team("Alabama", seed=2), Team("Robert Morris", seed=15)),

    # MIDWEST REGION
    (Team("Houston", seed=1), Team("SIU Edwardsville", seed=16)),
    (Team("Gonzaga", seed=8), Team("Georgia", seed=9)),
    (Team("Clemson", seed=5), Team("McNeese", seed=12)),
    (Team("Purdue", seed=4), Team("High Point", seed=13)),
    (Team("Illinois", seed=6), Team("Texas/Xavier", seed=11)),
    (Team("Kentucky", seed=3), Team("Troy", seed=14)),
    (Team("UCLA", seed=7), Team("Utah St.", seed=10)),
    (Team("Tennessee", seed=2), Team("Wofford", seed=15)),
]


# Define a function named 'simulate_game' that takes two arguments: 'team1' and 'team2'.
def simulate_game(team1, team2):
    # Check if the seed values of both teams are equal.
    if team1.seed == team2.seed:
        # If seeds are equal, randomly select and return one of the two teams as the winner.
        return random.choice([team1, team2])

    # Check if 'team1' has a higher seed value than 'team2'.
    if team1.seed > team2.seed:
        # If 'team1' has a higher seed (indicating a weaker rank), return 'team2' as the winner.
        return team2

    # If none of the above conditions are met (i.e., 'team1' has a lower seed than 'team2'),
    # return 'team1' as the winner.
    return team1


# Extract the first matchup (a tuple containing two Team objects) from the first round matchups list.
first_matchup = first_round[0]

# Print the first matchup to display the two teams involved in the game.
print(first_matchup)

# Simulate a game between the first team in the first matchup ("Auburn")
# and the first team in the second matchup ("Louisville").
# Note: Accessing `first_round[1][0]` ensures only the first Team object ("Louisville")
# from the second matchup tuple is passed to the function.
winner = simulate_game(first_matchup[0], first_round[1][0])

# Print the winner of the simulated game to the terminal.
print(winner)


# Define a function 'simulate_tournament' to simulate a full tournament
# starting from the first round matchups.
def simulate_tournament(first_round):
    # Initialize the current set of games to be the first round matchups.
    current_games = first_round

    # Continue looping until there are no more games to simulate.
    while len(current_games) > 0:
        # Print a message to indicate the start of a new round in the tournament.
        print("\n===== NEW ROUND =====")

        # Create a list to store the winners of each game in the current round.
        winners = []

        # Iterate through each matchup (pair of teams) in the current round.
        for team1, team2 in current_games:
            # Simulate a game between 'team1' and 'team2' to determine a winner.
            winner = simulate_game(team1, team2)
            # Add the winning team to the 'winners' list.
            winners.append(winner)

        # If there's only one winner left, return the final winner as the tournament champion.
        if len(winners) == 1:
            return winners[0]

        # Create a list to store the next round's matchups.
        next_round = []
        # Iterate through the list of winners in pairs (two at a time).
        for i in range(0, len(winners), 2):
            # Create a new matchup by pairing adjacent winners and add it to the next round.
            next_round.append((winners[i], winners[i + 1]))
            # [1,2,3,4,5,6]
            # [(1,2), (3,4), (5,6)]

        # Update 'current_games' to be the newly formed next round matchups.
        current_games = next_round

    # Return None if no champion is determined (this should never occur in a valid tournament).
    return None
