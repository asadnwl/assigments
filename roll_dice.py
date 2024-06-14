import random

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = int(input("Enter number of players (2-4): "))

    if 2 <= players <= 4:
        print(f"You are {players} players.")
        break
    else:
        print("Enter a valid number! (2 - 4)")
    
max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) <= max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1} roll a dice.\n")
        print("Total Score is ",player_score[player_idx])

        current_score = 0

        while True:
            should_roll = input("Would you play (y): ")
            if should_roll.lower() != 'y':
                break
            value = roll()
            if should_roll == 1:
                print("You entered 1.")
                current_score = 0
            else:
                current_score += value
                print(f"You rolled a {value}.")
            print(f"Your current score is {current_score}")
    
        player_score[player_idx] += current_score
        print("Your total score is", player_score[player_idx])

max_score = max(player_score)
winning_index = player_score.index(max_score)

print(f"Player {winning_index + 1} is the winner with a score of: {max_score}")