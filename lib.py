import random


def movie(movies):
    """Recommend a movie"""
    return random.choice(movies)


def song(songs):
    """Recommend a song"""
    return random.choice(songs)


def video_game(genre, games):
    """Recommend a video game by genre"""
    for current_genre, names in games.items():
        if current_genre == genre:
            return random.choice(names)


def joke(jokes):
    """Tell a joke"""
    return random.choice(jokes)


def story(stories):
    """Tell a story"""
    return random.choice(stories)


def guess_the_number(number):
    """Realize a guess the number game"""
    computer_number = random.randint(1, 10)
    print("\tComputer number:", computer_number)

    if number == str(computer_number):
        print("You guessed")
    elif number not in [str(num) for num in range(1, 11)]:
        print("I didn't understand, enter a number from 1 to 10")
    else:
        print("You not guessed the number")


def rock_paper_scissors(choice):
    """Realize the game rock scissors paper"""
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("\tComputer choice:", computer_choice)

    if choice == 'rock' and computer_choice == 'paper':
        print("You lost")
    elif choice == 'rock' and computer_choice == 'scissors':
        print("You win")
    elif choice == 'paper' and computer_choice == 'rock':
        print("You win")
    elif choice == 'paper' and computer_choice == 'scissors':
        print("You lost")
    elif choice == 'scissors' and computer_choice == "rock":
        print("You lost")
    elif choice == 'scissors' and computer_choice == "paper":
        print("You win")
    elif choice not in ["rock", "paper", "scissors"]:
        print("Sorry, I didn't understand your")
    else:
        print("we're tied")
