import random


def movie(movies):
    """Recommend a movie"""
    return random.choice(movies)


def song(songs):
    """Recommend a song"""
    return random.choice(songs)


def video_game(genre, games):
    """Recommend a video game by genre"""
    result = []
    for game in games:
        for name, current_genre in game.items():
            if current_genre == genre:
                result.append(name)

    if len(result) == 0:
        return "Sorry, I didn't"
    else:
        return random.choice(result)


def joke(jokes):
    """Tell a joke"""
    return random.choice(jokes)


def story(stories):
    """Tell a story"""
    return random.choice(stories)


def guess_the_number(number):
    """Realize a guess the number game"""
    computer_number = random.randint(1, 10)
    print("Computer number:", computer_number)

    if number == computer_number:
        print("You guessed")
    else:
        print("You lost")


def rock_paper_scissors(choice):
    """Realize the game rock scissors paper"""
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer choice:", computer_choice)

    if choice == computer_choice:
        print("You won")
    else:
        print("You lost")
