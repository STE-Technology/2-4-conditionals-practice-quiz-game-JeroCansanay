"""
File: quiz.py
Author: Name
Date: YYYY-MM-DD
Description: A Multiple choice game that calculates the score
"""
print("Multiple-Question Quiz Game (NBA)")

correct_answers = 0

print("1. Who scored the most career points in the NBA?")
print("(a) Michael Jordan")
print("(b) Lebron James")
print("(c) Kareem Abdul-Jabbar")

answer_1 = input("Answer:")

if answer_1.lower() == "b":
    print("Correct!")
    correct_answers += 1
else:
    print ("Incorrect")

print("2. Who scored the most 3 career points in the NBA?")
print("(a) Stephen Curry")
print("(b) Ray Allen")
print("(c) Kyle Korver")

answer_2 = input("Answer:")

if answer_2.lower() == "a":
    correct_answers += 1
    print("Correct!")
else:
    print("Incorrect!")

print("3. Who scored the most points in a single NBA game?")
print("(a) Lebron James")
print("(b) Kareem Abdul-Jabbar")
print("(c) Kobe Bryant")

answer_3 = input("Answer:")

if answer_3.lower() == "b":
    correct_answers += 1
    pri

# Calculate the percentage score
score_percentage = (correct_answers / 3) * 100

# Print the quiz completion message with the score
print("Quiz complete! You answered {} out of 3 questions correctly. Your score is {:.1f}%".format(correct_answers, score_percentage))