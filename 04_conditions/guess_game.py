def get_guess():
    guess = input("Enter a guess: ").strip().lower()
    return guess 

def main():
    guess = get_guess()
    if guess == "50" or guess == "fifty":
        print("Correct!")
    else:
        print("Incorrect!")

main()