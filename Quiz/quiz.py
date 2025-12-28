score_count = 0

questions = [
    "What is the capital of Nigeria? ",
    "Which African country has a state called 'Lagos' in it? ",
    "In what continent is Scotland? ",
    "How many grams make one kilogram? "
]

correct_ans = [
    "Abuja",
    "Nigeria",
    "Europe",
    "1000 grams"
]

for i in range(len(questions)):
    answer = input(questions[i])

    clean = answer.lower().strip().replace(" ", "")
    correct_clean = correct_ans[i].lower().replace(" ", "")

    if clean == correct_clean:
        print("Bravo!! You are right")
        score_count += 1
    else:
        print("No luck at the moment, Try again")

print("Quiz ends here!!!")
print("Score:", score_count)