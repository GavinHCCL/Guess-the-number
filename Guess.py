import random
from sympy import primefactors


numbers = []

for number in range(10,100):
    numbers.append(number)
    answer = random.choice(numbers)

#print(answer)
#print(numbers)

program = "running"


while program == "running":
    question = input("Input >> ")

    if question == f"{answer}":
        print("Correct! You Won!")
        program = "stopped"
    if question != f"{answer}":
        print("Incorrect, Hint: Some of the prime factors of this number are...")
        print(f"{primefactors(answer)}")

if program == "stopped":
    print("stopping")