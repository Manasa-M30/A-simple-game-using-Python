import random

print("Welcome to Zombie, Vampire, Human Game!")
player1_name = input("Enter Player 1's name: ")
player2_name = input("Enter Player 2's name: ")

choices = ["zombie", "vampire", "human"]
player1_score = 0
player2_score = 0

while True:
    play_game = input("Do you want to play the game? (yes/no): ").lower()
    if play_game != "yes":
        break
    
    player1 = input(player1_name + ", choose Zombie, Vampire, or Human (your choice will be hidden): ").lower()
    print("\n" * 50)  
    
    if player1 not in choices:
        print("Invalid choice. Please choose Zombie, Vampire, or Human.")
        continue
    
    player2 = input(player2_name + ", choose Zombie, Vampire, or Human: ").lower()
    if player2 not in choices:
        print("Invalid choice. Please choose Zombie, Vampire, or Human.")
        continue
    
    print(f"{player1_name} chose: {player1}")
    print(f"{player2_name} chose: {player2}")

    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "zombie" and player2 == "human") or \
         (player1 == "human" and player2 == "vampire") or \
         (player1 == "vampire" and player2 == "zombie"):
        print(f"\U0001F389 {player1_name} wins this round!")
        player1_score += 1
    else:
        print(f"\U0001F389 {player2_name} wins this round!")
        player2_score += 1

print("\nGame Over!")
print(f"Final Score: {player1_name} - {player1_score} | {player2_name} - {player2_score}")
