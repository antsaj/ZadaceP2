from csv import reader

with open('rezultati.csv', 'r',encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    list_of_tuples = list(map(tuple, csv_reader))
list_of_tuples.sort(key=lambda x: x[1])
print(list_of_tuples)

a=0
b=0
c=0
d=0
e=0

ocjene={
"izvrstan":a,
"vrlo dobar":b,
"dobar":c,
"dovoljan":d,
"nedovoljan":e,
    }

for ime,prezime,bodovi in list_of_tuples:
    if int(bodovi)>=0 and int(bodovi)<50:
        e=e+1
        ocjene["nedovoljan"]=e
    if int(bodovi)>=50 and int(bodovi)<65:
        d=d+1
        ocjene["dovoljan"]=d
    if int(bodovi)>=65 and int(bodovi)<80:
        c=c+1
        ocjene["dobar"]=c
    if int(bodovi)>=80 and int(bodovi)<90:
        b=b+1
        ocjene["vrlo dobar"]=b
    if int(bodovi)>=90 and int(bodovi)<100:
        a=a+1
        ocjene["izvrstan"]=a
        
print(ocjene)
