angka = int(input("Masukkan angka : "))

# Cara 1
# if(angka % 2 == 0) :
#     print("Angka " + str(angka) + " tergolong bilangan GENAP")
# else :
#     print("Angka " + str(angka) + " tergolong bilangan GANJIL")

# Cara 2
# if((angka/2).is_integer()) :
#     print("Angka " + str(angka) + " tergolong bilangan GENAP")
# else :
#     print("Angka " + str(angka) + " tergolong bilangan GANJIL")

# Cara 3
arr = ['GENAP', 'GANJIL']

print("Angka {} tergolong bilangan {}".format(angka, arr[angka%2]))

# a = 6
# b = 2
# c = a / b

# print(c)
# print(type(c))
