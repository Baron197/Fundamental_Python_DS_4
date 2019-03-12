x = [6000, 34, 203, 3, 746]

def bubbleSort(list) :
    for i in range(len(list)-1, 0, -1) :
        for j in range(i) :
            if (list[j] > list[j + 1]) :
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(bubbleSort(x))


