import game_data
import random

# TODO Make a function to get data from array
def get_data():
    """Returns a random item from the game_data array"""
    data_item = random.choice(game_data.data)
    return data_item

# TODO When setting the second choice make sure that the same data doesn't load for both choices
def set_choice_2(other_choice):
    """Returns a random item from the game_data array that is not equal to the argument given"""
    new_choice = get_data()
    if new_choice != other_choice:
        return new_choice
    else:
        return set_choice_2(other_choice)

# TODO Set data to 2 variables when game starts
choice_1 = get_data()
choice_2 = set_choice_2(choice_1)

playing = True
streak = 0

# TODO Make a game loop to have the player compare the number of followers in the data set
while playing:
    print("Who do you think has more followers on Intagram:")
    print(f"A:{choice_1["name"]}, {choice_1["description"]} from {choice_1["country"]} \nor")
    print(f"B: {choice_2["name"]}, {choice_2["description"]} from {choice_2["country"]} \n")

    guess = choice_1
    other = choice_2
    input_invalid = True

    while input_invalid:
        try:
            user_input = input("Type 'A' or 'B': ").lower()
        except TypeError:
            user_input = "c"
        if user_input == "a":
            input_invalid = False
        elif user_input == "b":
            guess = choice_2
            other = choice_1
            input_invalid = False
        else:
            print("Invalid input. Try again.")

# TODO If the player is wrong end the game
    if int(guess["follower_count"]) < int(other["follower_count"]):
        print("Sorry!")
        print(f"{guess["name"]} has {guess["follower_count"]}k followers and {other["name"]} has {other["follower_count"]}k followers")
        print(f"You got {streak} right")
        playing = False

# TODO If the player is right then make the first choice equal the second and the second choice a new choice
    else:
        print("Good job!")
        print(f"{guess["name"]} has {guess["follower_count"]}k followers and {other["name"]} has {other["follower_count"]}k followers")
        streak += 1
        print(f"You've gotten {streak} right so far")
        choice_1 = choice_2
        choice_2 = set_choice_2(choice_1)
