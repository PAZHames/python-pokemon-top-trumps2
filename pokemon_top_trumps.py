import requests
from pprint \
    import pprint
import random

# Random Pokemon function


def get_random_pokemon():
    random_integer = random.randint(1, 151)
    pokemon_number = random_integer
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
    response = requests.get(url)
    pokemon = response.json()
    return pokemon


def display_result(player_wins, opponent_wins):
    if player_wins > opponent_wins:
        print(f"{player_wins}-{opponent_wins} to you! You win the match! You've caught them all!")
    else:
        print(f"{opponent_wins}-{player_wins} to your opponent! You have been defeated! Better luck next time!")


player_wins = 0
opponent_wins = 0
games_played = 0

name = input("What is your name?")

for _ in range(6): # for loop so the game runs 5 times (hopefully) before printing result

############################## PLAYER POKEMON #############################

# generate 3 random pokemon - enter into array

    pokemon_options = []
    for _ in range(3):
        pokemon = get_random_pokemon()
        pokemon_options.append(pokemon)

    # for pokemon in pokemon_options:
    #     print(f'Pokemon ({pokemon_options[i]+1})\nName: {pokemon["name"]},\nID: {pokemon["id"]},\nHeight: {pokemon["height"]},\nWeight: {pokemon["weight"]}')


# get player's choice

    choice = int(input("Choose your fighter! (1-3)"))

    if choice in range(1, 4):
        chosen_pokemon = pokemon_options[choice-1]
        height = chosen_pokemon["height"]*10 #converting from decimeters to cm
        weight = chosen_pokemon["weight"]/10 #converting from hectograms to kilograms
        print(f'Your Pokemon -\nName: {chosen_pokemon["name"]},\nID: {chosen_pokemon["id"]}/128,\nHeight: {height}cm,\nWeight: {weight}kg')
    else:
        print(f'Number outside range :(')
        continue
        # so this guy doesn't blow the whole game

############################## COMPUTER POKEMON #############################

    opponent_pokemon = get_random_pokemon()

# print(f'Opponent Pokemon -\nName: {opponent_pokemon["name"]},\nID: {opponent_pokemon["id"]},\nHeight: {opponent_pokemon["height"]},\nWeight: {opponent_pokemon["weight"]}')

    # player chooses stat
    chosen_stat = input("Which stat do you want to use? (id/height/weight)")

    # put stat to lower case
    stat = chosen_stat.lower().replace(" ","")

    # create tally for who wins


#################### RESULTS ####################################

    if games_played in range(0,5):
# if no of games if 4 we play again, but if it's 5 we stop
        if stat == "id":
            if chosen_pokemon["id"] > opponent_pokemon["id"]:
                print(f"You win!")
                player_wins += 1
            else:
                print(f"You lose!")
                opponent_wins += 1

        elif stat == "height":
            if chosen_pokemon["height"] > opponent_pokemon["height"]:
                print(f"You win!")
                player_wins += 1

            else:
                print(f"You lose!")
                opponent_wins += 1

        elif stat == "weight":
            if chosen_pokemon["weight"] > opponent_pokemon["weight"]:
                print(f"You win!")
                player_wins += 1

            else:
                print(f"You lose!")
                opponent_wins += 1
        else:
            print(f"Stat not recognised... you lose anyway... very sad")

        games_played += 1

display_result(player_wins, opponent_wins)

# initially did it twice then put into a function