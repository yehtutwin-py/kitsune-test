import random
attempts = 0
print("Welcome to the Number Guessing Game!")
while True:
    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if difficulty == "easy":
            num = random.randint(1, 50)
            print("You have chosen Easy difficulty. Guess a number between 1 and 50.")
            break
        elif difficulty == "medium":
            num = random.randint(1, 100)
            print("You have chosen Medium difficulty. Guess a number between 1 and 100.")
            break
        elif difficulty == "hard":
            num = random.randint(1, 200)
            print("You have chosen Hard difficulty. Guess a number between 1 and 200.")
            break
        else:
            print("Invalid difficulty level. Please choose again.")
            continue
    print("Max attempts: 10")
    while True:
        guess = int(input("Enter your winning guess: "))
        if attempts > 10:
            print(f"Max 10 attempts! \nGame Over! The correct number was {num}.")
            attempts = 0
            replay = input("Replay the game to try again! (Y/N): ")
            if replay.lower() == "y":
                attempts = 0
                break
            else:
                exit()
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

        