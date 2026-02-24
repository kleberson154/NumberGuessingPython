import random

best_score = None

play_again = "yes"
while play_again.lower() == "yes":
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed_correctly:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                guessed_correctly = True
        except ValueError:
            print("Please enter a valid number.")

    if best_score is None or attempts < best_score:
        best_score = attempts
        print(f"🏅 New record! Fewest attempts: {best_score}")
    else:
        print(f"Your best score remains: {best_score} attempts.")

    play_again = input("Want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing! Come back soon!")