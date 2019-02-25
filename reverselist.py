import math

def reverseList(theList) :
    for i in range(0, math.floor(len(theList)/2)) :
        theList[i], theList[len(theList) - 1 - i] = theList[len(theList) - 1 - i], theList[i]

    return theList

# def reverseList(theList) :
#     for i, j in zip(
#         range(0, math.floor(len(theList)/2)),
#         range(len(theList)-1,math.ceil(len(theList)/2)-1,-1)
#         ) :
#         theList[i], theList[j] = theList[j], theList[i]
        
#     return theList

print(reverseList([1,2,3,4,5,6,7,8,9]))


# for i,j in zip(range(5),['hello','sultan','bartolomeo']) :
#     print('i : {}'.format(i))
#     print('j : {}'.format(j))
