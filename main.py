import random
from data_lib import *


def greeting():
    """Prints a greeting in the console."""
    print("\nWelcome to Higher-Lower game! :)")


def randomize_candidate_B(a):
    """Takes candidate_A (str). Randomly chooses another candidate from
    data, first checks if it was different from candidate_A.
    Also checks if candidate_A has same "follower_count" value as candidate_B.
    In that case, picks another.
    Returns candidate_B (str)."""
    b = random.choice(data)
    if a == b:
        while not a != b and a["follower_count"] != b["follower_count"]:
            b = random.choice(data)
    return b


def print_candidates(a, b):
    """Prints candidate_A and candidate_B in the console."""
    print("\nA: {} - {} from {}.".format(a["name"], a["description"], a["country"]))
    print("[vs.]")
    print("B: {} - {} from {}.".format(b["name"], b["description"], b["country"]))


def take_input():
    """Asks for user input. Eliminates invalid inputs.
    Returns "a" or "b"."""
    x = input('\nWhich one has more followers? Input "A" or "B": ').lower()
    while x not in ["a", "b"]:
        x = input('Invalid input. Please, type "A" or "B": ')
    return x


def guess_correct(u, a, b):
    """Checks if the user guessed correctly.
    Returns True or False."""
    if u == "a":
        if a["follower_count"] > b["follower_count"]:
            return True
    elif u == "b":
        if b["follower_count"] > a["follower_count"]:
            return True
        return False


def another_game():
    """Takes user input "y" or "n". Eliminates invalid inputs.
    Returns True or False."""
    x = input('\nDo you wanna play again? Type "Y" or "N": ').lower()
    while x not in ["y", "n"]:
        x = input('Invalid input. Please, type "Y" or "N": ').lower()
    if x == "y":
        return True
    return False


###############################################################################
score = 0
program_running = True
game_over = False

greeting()

candidate_A = random.choice(data)

while program_running:
    while not game_over:
        candidate_B = randomize_candidate_B(candidate_A)
        print_candidates(candidate_A, candidate_B)
        user_input = take_input()
        if guess_correct(user_input, candidate_A, candidate_B):
            score += 1
            print("\nYou guessed correctly! Your score: {}".format(score))
            candidate_A = candidate_B
        else:
            print("\nYou guessed wrong. {} has {}.000 followers, while {} has {}.000.".format(candidate_A["name"],
                                                                                              candidate_A["follower_count"],
                                                                                              candidate_B["name"],
                                                                                              candidate_B["follower_count"]))
            print("Game over. Your final score: {}".format(score))
            game_over = True

    if another_game():
        game_over = False
    else:
        program_running = False

print("\nGoodbye! :)")