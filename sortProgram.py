arr = []

def MainMenu() :
    pilihan = int(input("Menu : \n 1. See Array \n 2. Input Array \n 3. Sort Array \n 4. Min Max Value \n 5. Exit \nYour Choice? : "))
    return pilihan

def SeeArray() :
    print('Isi Array : ')
    print(arr)

def InputArray() :
    angka = int(input("Number : "))
    arr.append(angka)

def Ascending(a,b) :
    return a - b

def Descending(a,b) :
    return b - a

arahSort = [Ascending,Descending]

def SortArray() :
    arah = int(input("Input 1 untuk Ascending dan 2 untuk Descending : "))
    for i in range(len(arr)-1) :
        for j in range(i+1, len(arr)) :
            if(arahSort[arah-1](arr[i], arr[j]) > 0) :
                temp = arr[i]
                arr[i] = arr[j] 
                arr[j] = temp 

def MinMaxArray() :
    minNum = arr[0]
    maxNum = arr[0]
    for num in arr[1:] :
        if(num < minNum) :
            minNum = num
        if(num > maxNum) :
            maxNum = num
    print("Min : {} and Max : {}".format(minNum,maxNum))

kumpulanFunction = [SeeArray,InputArray,SortArray,MinMaxArray]

while(True) :
    pilihan = MainMenu()
    if(pilihan == 1 or pilihan == 2 or pilihan == 3 or pilihan == 4) :
        kumpulanFunction[pilihan-1]()
    elif(pilihan == 5) :
        print('Sampai Jumpa Lagi!')
        break
