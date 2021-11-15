# Coding rock paper scissors game with python.

import random

while True:
    def play_game():
        user = input("pick your choice - Rock(r), Paper(p), Scissors(s) to play: ")
        computer = random.choice(["r", "p", "s"])

        if user == computer:
            return "It's a tie"

        if win(user, computer):
            return "You won!"
        else:
            return "You lost!"


    def win(player, opponent):
        if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") \
                or (player == "s" and opponent == "p"):
            return True

        if player == "exit":
            exit()


    print(play_game())
