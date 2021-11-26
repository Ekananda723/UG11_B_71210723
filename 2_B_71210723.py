#reminder
string = "abc"
inter = 123

#data
def check_data_type(jenis, tipe):
    typ = tipe.lower()
    if (type(jenis) == type(string)) and (typ == "str"):
        print("Jawaban Anda benar")
        return "True"
    elif(type(jenis) == type(string)) and (typ == "int"):
        print("Jawaban Anda salah, seharusnya adalah: str")
        return "False"
    elif(type(jenis) == type(inter)) and (typ == "int"):
        print("Jawaban Anda benar")
        return "True"
    elif (type(jenis) == type(inter)) and (typ == "str"):
        print("Jawaban Anda salah, seharusnya adalah: int")
        return "False"    

print(check_data_type("Kevin","STr"))
print(check_data_type("Kevin","str"))
print(check_data_type(12345,"str"))
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))
