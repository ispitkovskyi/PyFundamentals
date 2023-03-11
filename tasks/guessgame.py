
secret_word = "giraffe"
guess = ""

guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_count += 1
        guess = input("Enter guess: ")
    else:
        out_of_guesses = True

if guess == secret_word:
    print("You win!")
else:
    print("You lose!")