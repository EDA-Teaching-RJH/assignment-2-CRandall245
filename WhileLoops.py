### Part Two -- your code goes here. 
import random

def main():
    goal = int(random.uniform(1,10)) #generates random number
    user = int(input("Guess the random number:")) #takes user input
    while user != goal: #loops until user input is the random number
        user = int(input("Guess the random number:")) 


main()