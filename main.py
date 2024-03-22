from lib import *
from data import *

while True:
    print("------------Welcome!------------\n\n"
          "1. Recommend some movie\n"
          "2. Recommend some song\n"
          "3. Recommend a video game by genre\n"
          "4. Tell me a joke\n"
          "5. Tell me an interesting story\n"
          "6. Let's play a game of guess the number\n"
          "7. Let's play a game of rock scissors paper\n"
          "8. Exit.")

    choice = input("Select your choice: ").strip()

    match choice:
        case "1":
            print(f"\nTitle: '{movie(movies)}', enjoy the movie!\n")
        case "2":
            current_song = song(songs)
            print(f"\n{current_song[0]} - '{current_song[1]}', enjoy the song!\n")
        case "3":
            print("\nAvailable genres:")
            for genre in genres:
                print("\t", genre)
            user_genre = input("\nChoice genre: ").lower().strip()

            if user_genre not in genres:
                print("Sorry, I didn't understand")
            else:
                print(f"Title: '{video_game(user_genre, games)}', hope you like it!\n")
        case "4":
            print(f"\n'{joke(jokes)}'\nAre you laughing?)\n")
        case "5":
            print("\n", story(stories), "\n")
        case "6":
            print("\nWelcome to the game!\nTry to guess a number from 1 to 10!")
            number = input("\tEnter your number: ").strip()
            guess_the_number(number)
            print()
        case "7":
            print("\nWelcome to the game rock scissors paper!")
            choose = input("\tEnter your choice: ").lower().strip()
            rock_paper_scissors(choose)
            print()
        case "8":
            break
        case _:
            print("\nSorry, I didn't understand, try again!\n")
