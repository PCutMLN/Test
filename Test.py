
# variable (variable adalah pemisalan)

nama = "Abiyyu" # string (string adalah objek yang berada di kuotasi)
umur = 15 # integer (integer adalah angka)
lakilaki = True # boolean (True/False)
tinggi = 140.6 # float

daftarnama = ["Abiyyu","Abiyyu1","Abiyyu2"] # array

introduksi = "Saya " + nama + ", saya berumur" + str(umur)
# Saya Abiyyu, saya berumur 15

if lakilaki:
    print("saya laki-laki")
else:
    print("saya perempuan")

panjang = len(daftarnama) # len digunakan untuk menghitung jumlah objek di array
daftarnama.append("Abiyyu4") # append digunakan untuk menambah objek ke array

print(panjang)
print(len(daftarnama))
print(daftarnama[3])

# function
# function name
# function body
# parameter (0 =< N) 
# return value (0 =< N)
def tambah(a, b):
    hasil = a + b
    return hasil

c = tambah(5, 4)
print("hasilnya adalah "+str(c))

# Percabangan
# if
n = 5
if n < 10:
    print("n adalah satuan")

# if else
if n < 10 and n > 0:
    print("n adalah satuan "+str(n))
else:
    print("n bukan satuan")

# if else if
b = -10
if b <= 0:
    print("b bukan negatif, b adalah "+str(b))
elif b < 10:
    print("b adalah satuan")
else:
    print("b lebih dari sama dengan 10")

# PERULANGAN
# iterasi
# for loop
i=0
for nama in daftarnama:
    # nama = daftarnama[index]
    i+=1 # -> i = i + 1
    print(str(i)+" == "+nama)