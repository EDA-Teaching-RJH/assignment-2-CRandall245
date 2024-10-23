### Part Four -- your code goes here. 
import random

def main():
    list = []
    for i in range(10):
        a = random.randint(1, 100)
        list.append(a)
    print(list)
    b = True
    i = 0
    while b == True:
        a = list.count(i)
        i = i + 1
        if i == 101:
            b = False
            print(list)
        elif (i - 1) % 2 != 0 and a == 1:
            re = list.index(i - 1)
            list.pop(re)
        elif (i - 1) % 2 != 0 and a > 1:
            while a != 0:
                re = list.index(i - 1)
                list.pop(re)
                a = a - 1
        else:
            b = True

main()

