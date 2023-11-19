myList = [1,3,5,6,10,22,42,42,42]
lengthOfMyList = len(myList)

for i in range(lengthOfMyList // 2):
    myList[i], myList[lengthOfMyList - i - 1] = myList[lengthOfMyList - i - 1], myList[i]
print(myList)