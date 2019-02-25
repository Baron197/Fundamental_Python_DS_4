def fibo(num) :
    theList = []
    for i in range(num) :
        if(i < 2) :
            theList.append(1)
        else :
            theList.append(theList[i-1] + theList[i-2])
    
    return theList

inputUser = int(input("Ukuran : "))

hasil = fibo(inputUser)
print(hasil)
if(len(hasil) > 0) :
    print("Output = {}".format(hasil[-1]))
else :
    print("Output = None")
    