import random


questions = {
    1 : {
        "question": "Print objects to the text stream file",
        "answer": "print"
    },
    2 : {
        "question": "Return the absolute value of a number",
        "answer": "abs"
    },
    3 : {
        "question": "Return the length (the number of items) of an object",
        "answer": "len"
    },
    4 : {
        "question": "Reads a line from the input (usually from the user), converts the line into a string by removing the trailing newline, and returns it",
        "answer": "input"
    },
    5: {
        "question": "A loop that is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)",
        "answer": "for"
    },
    6: {
        "question": "A loop that can execute a set of statements as long as a condition is true",
        "answer": "while"
    },
    7: {
        "question": "Are used to store multiple values in one single variable that can be altered",
        "answer": "arrays"
    },
    8: {
        "question": "Are used to store multiple values in one single variable but are immutable",
        "answer": "tuple"
    },
    9: {
        "question": "Are used to store data values in key:value pairs",
        "answer": "dictionary"
    },
    10: {
        "question": " ________ is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes",
        "answer": "python"
    }
}

score = 0

print("=========================")
print("|\tQUIZ GAME\t|")
print("=========================")
print("Instructions: Enter the answer for each question")
print("Note: All questions and answer are related to Python or Software Engineering\n")

random_questions = list(questions.keys())
random.shuffle(random_questions)
question_number = 0
for question in random_questions:
    question_number += 1
    print(f"{question_number}. {questions[question]['question']}")
    answer = input("Enter answer: ")
    if answer.lower() == questions[question]['answer'].lower():
        score += 1
        print("Correct!")
    else:
        print("Wrong answer!")
    print(f"You got {score} out of {len(questions)}\n")

if score >= 5:
    print("You passed the quiz! Congratulations!")
else:
    print("You failed the quiz! I hope you learned new things here for your next quiz.")