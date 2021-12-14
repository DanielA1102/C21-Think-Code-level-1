# -------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("GOED!")
        return 1
    else:
        print("FOUT!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTATEN")
    print("-------------------------")

    print("Antwoorden: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("gissingen: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("jou score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Wil je nog een keer spelen?? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Wie heeft Python gemaakt??: ": "A",
 "In welk jaar is Python gemaakt??: ": "B",
 "Python is een eerbetoon aan welke comedygroep?: ": "C",
 "Is de aarde rond?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. wat is de aarde?"]]

new_game()

while play_again():
    new_game()

print("TOT ZIENS!")

# -------------------------