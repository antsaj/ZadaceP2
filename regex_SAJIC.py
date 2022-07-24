
#ime.prezime@fpmoz.sum.ba
print("pazite na unos velikih i malih slova imena i prezimena!")
email=input("unesite svoj fpmoz email: ")
regex="[a-zA-z]*\.[a-zA-z]*@fpmoz\.sum\.ba"
ime="[a-zA-z]*"
rezultat_imena=re.findall(ime,email)
rijec_imena=rezultat_imena[0]
result=re.findall(regex,email)

prezime=rezultat_imena[2]
slovo_imena=rijec_imena[0]

if not result:
    print("neispravan email!")
else:
    print("uspiješan unos maila")

    
#iprezimeX@sum.ba
eduid=input("unesite svoj edu id: ")
reg="[a-zA-z]*\d*@sum\.ba"
regx="[a-zA-z]*"
rez=re.findall(reg,eduid)
rezu=re.findall(regx,eduid)
rijec=rezu[0]
provjera_imena=rijec[0]
provjera_prezimena=rijec[1:]

regex2=slovo_imena+prezime+".*"
resul=re.findall(regex2,eduid)


if provjera_imena==slovo_imena:
    if resul:
        if not rez:
            print("neispravan eduid!")
        else:
            print("uspješan unos edu id-a")
    else:
        print("ne podudaraju se prezimena")
else:print("ne podudaraju se imena")


