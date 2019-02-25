# t = (1, [0, "test"], { "a1" : True })

# print(t[2]["a1"])
# print(t[1][1])
# t[1][1] = "akan"
# print(t[1][1])
# t[1] = "mark"
# print(t[1])

# s = { 5,7,3,4,5,3,3,2,3,"test","test","kari",True,False }

# print(s)
# print(list(s)[1])

# newList = [1,2,3,4,5]
# for i in range(len(newList)) :
#     newList[i] = "Manusia {}".format(newList[i] * 2)

# print(newList)

# newList = [1,2,3,4,5]
# newList = ["Manusia {}".format(item*2) for item in newList]
# print(newList)

# arrManusia = [
#     {
#         "nama": "Baron",
#         "umur": 22,
#         "pekerjaan": "Guru"
#     },
#     {
#         "nama": "Malware",
#         "umur": 90,
#         "pekerjaan": "Tukang Menyakiti orang"
#     },
#     {
#         "nama": "Supriman",
#         "umur": 150,
#         "pekerjaan": "Wrestling Champion"
#     }
# ]

# def Ceritakan(dataManusia) :
#     return "Namanya {}, dia berumur {}, dan dia bekerja sebagai {}".format(dataManusia["nama"]
#     ,dataManusia["umur"],dataManusia["pekerjaan"])

# # arrCerita = list(map(Ceritakan, arrManusia))
# arrCerita = [Ceritakan(item) for item in arrManusia]

# print(arrCerita)
# for i in range(len(arrCerita)) :
#     print('Cerita {} : '.format(i+1))
#     print(arrCerita[i])

newDict = { "kerja": 50 }

newDict["karimun"] = ['hello', 100]

print(newDict)