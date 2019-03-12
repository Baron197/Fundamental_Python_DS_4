def sorting(arr, fn) :
    for i in range(len(arr)-1) :
        for j in range(i+1, len(arr)) :
            if(fn(arr[i],arr[j]) > 0) :
                arr[i],arr[j] = arr[j],arr[i]
    return arr

def ascending(a,b) :
    return a - b
def descending(a,b) :
    return b - a

theList = [5,32,5,2,6,5,3,8,23,1]

theList = sorting(theList, ascending)
print(theList)

a = 23

for i,j in zip(range(0,6,2), [3,2,6,1]) :
    for k in range(j) :
        a -= j
    for l, m in zip(range(i), range(len([2,1,4,6]))) :
        if(m > 1) :
            a += 2
            if(l < 3) :
                a += 3
            for n in range(4) :
                a += 1
    a += 1

print(a)

def tambah(a,b) :
    return a + b

def tambah(a,b,c=0) :
    return a + b + c

tambahlamb = [lambda a,b,c=0 : a+b+c]

print(tambahlamb[0](b=2,a=4))

