import random
win_count = 0
lose_count = 0


def play():

    user_input = input("What is your choice? R for Rock, P for Paper, S for Scissors.\n").lower()
    computer_input = random.choice(["r", "p", "s"])
    global win_count
    global lose_count

    if user_input == computer_input:
        print("It's a tie!")
        return playagain()

    # R > S, S > P, P > R

    if iswin(user_input, computer_input):
        print("You win")
        win_count += 1
        return playagain()
    elif valueerror(user_input):
        print("\nThat is an invalid input, please try again.\n")
        return play()

    else:
        print("\nYou lose")
        lose_count += 1
        return playagain()


def iswin(user, computer):
    if user == "r" and computer == "s" or user == "s" and computer == "p" or user == "p" and computer == "r":
        return True


def valueerror(user):
    acceptable_inputs = ["r", "p", "s"]
    if user not in acceptable_inputs:
        return True


def playagain():
    user_input = input("Do you want to play again? Y for yes, N for no.\n").lower()
    acceptable_inputs = ["y", "n"]
    if user_input == "n":
        print("Thank you for playing!")
        print("Your overall score was " + str(win_count) + " win(s) and " + str(lose_count) + " loss(es)")
    elif user_input not in acceptable_inputs:
        print("\nThat is an invalid input, please try again.\n")
        return playagain()
    return play()

play()