def obrni(string):
    if len(string)==0:
        return " "
    return string[-1]+obrni(string[:-1])
    

string=input("unesi string koji zelite obrnit: ")
print(obrni(string))
