import random

# Range limits
ln = 0
hn = 5
ans = random.randint(ln, hn)
guesses = 0
run = True

print("---------RANDOM NUMBER GUESSING GAME---------")
print(f"Enter a number between {ln} and {hn}")

while run:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < ln or guess > hn:
            print("❌ Out of range. Try again.")
        elif guess < ans:
            print("🔻 TOO LOW. TRY AGAIN!")
        elif guess > ans:
            print("🔺 TOO HIGH. TRY AGAIN!")
        else:
            print("✅ CORRECT GUESS!")
            run = False
    else:
        print("⚠️ Invalid input. Please enter a number.")

print(f"🎯 Total number of guess(es): {guesses}")
