### Part Two -- your code goes here. 
import random

def main():
    goal = int(random.uniform(1,10))
    user = int(input("Guess the random number:"))
    while user != goal:
        user = int(input("Guess the random number:"))


main()