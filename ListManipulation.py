### Part Three -- your code goes here. 


def main():
    list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    list.sort()
    i = 0
    count = list.count(1)
    while i < count:
        i = i + 1
        list.pop(list.index(int(1)))
    addlist = [7, 8]
    list.extend(addlist)
    print(list)

main()