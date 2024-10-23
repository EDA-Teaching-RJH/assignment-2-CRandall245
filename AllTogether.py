### Part Four -- your code goes here. 
import random

def main():
    list = []
    for i in range(10): #this for generates a list of 10 random numbers
        a = random.randint(1, 100)
        list.append(a)
    print(list)
    b = True
    i = 0
    while b == True: #this while loops until i is outside the random number range
        a = list.count(i) #finds the number of int i in the list
        i = i + 1
        if i == 101:
            b = False
            print(list)
        elif (i - 1) % 2 != 0 and a == 1: #if there is a single number of i in the list and its odd it removes the i from the list
            re = list.index(i - 1)
            list.pop(re)
        elif (i - 1) % 2 != 0 and a > 1: #if there multiple number of i in the list and its odd it removes all the i from the list
            while a != 0:
                re = list.index(i - 1)
                list.pop(re)
                a = a - 1
        else: #if i isnt in the list or even continues the while loop
            b = True

main()

