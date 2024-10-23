### Part Three -- your code goes here. 


def main():
    list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] #creates list
    list.sort() #sorts list
    i = 0 #counter varaible
    count = list.count(1) #finds the number of 1s
    while i < count: 
        i = i + 1   #+1 counter variable
        list.pop(list.index(int(1))) #removes 1s from list
    addlist = [7, 8]
    list.extend(addlist) #adds onto the end of main list
    print(list)

main()