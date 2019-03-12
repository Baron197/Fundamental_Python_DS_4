from math import floor

x = [ 1,2,3,2,5,2,7,2 ]

# function mean

def getMean(list) :
    sum = 0
    for item in list :
        sum += item

    mean = sum / len(list)
    return mean
print(getMean(x))

# function median

def getMedian(list) :
    list.sort()
    median = 0
    if (len(list) % 2 != 0) :
	    median = list[floor(len(list) / 2)]
    else :
        mid1 = list[(int(len(list) / 2)) - 1]
        mid2 = list[int(len(list) / 2)]
        median = (mid1 + mid2) / 2
    return median

print(getMedian(x))

# function mode

def getMode(list) :
    countDictionary = {}
    # create countDictionary
    for num in list :
        if(num in countDictionary.keys()) :
            countDictionary[num] += 1
        else :
            countDictionary[num] = 1
    # create list of mode/s
    maxFrequency = 1
    modes = []
    for key in countDictionary :
        if (countDictionary[key] > maxFrequency) :
            modes = [key]
            maxFrequency = countDictionary[key]
        elif (countDictionary[key] == maxFrequency) :
            modes.append(key)
    # if every value appears same amount of times
    if (len(modes) == len(countDictionary.keys())) :
        modes = []
    return modes

print(getMode(x))

