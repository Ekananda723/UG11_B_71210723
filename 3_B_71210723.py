kalimat = input("Masukkan kalimat awal: ")
kata = input("Masukkan kata untuk disisipkan: ")
index = int(input("Masukkan index: "))
real_index = index - 1

def sisip(kalimat, kata, index):
    print(kalimat[:real_index] + kata + kalimat[real_index:])
    
sisip(kalimat ,kata ,index)
