import random
attempts = 0
print("Welcome to the Number Guessing Game!")
while True:
    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if difficulty == "easy":
            num = random.randint(1, 50)
            break
        elif difficulty == "medium":
            num = random.randint(1, 100)
            break
        elif difficulty == "hard":
            num = random.randint(1, 200)
            break
        else:
            print("Invalid difficulty level. Please choose again.")
            continue
    while True:
        print("Max attempts: 10")
        guess = int(input("Enter your winning guess: "))
        if attempts > 10:
            print(f"Max 10 attempts! \nGame Over! The correct number was {num}.")
            attempts = 0
            break
        elif guess > num:
            print("Too High! Try Again.")
            attempts += 1
        elif guess < num:
            print("Too Low! Try Again.")
            attempts += 1
        else:
            print("Congratulations! You guessed the number!")
            attempts += 1
            print(f"You guessed the number in {attempts} attempts.")
            print("Thank you for playing the Number Guessing Game!")
            replay = input("Replay the game to try again! (Y/N): ")
            if replay.lower() == "y":
                attempts = 0
                continue
            else:
                exit()

        