#input
kalimat = input("Masukkan kalimat untuk dihitung: ")
panjang = len(kalimat)

#data
def hasil(panjang):
    return int(panjang*(2/3))

hasil(panjang)
print(hasil(panjang))
