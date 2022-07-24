import random
imena=['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena=['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez',
'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith',
'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']


radnici=[]
for i in range(15):
    radnik={}
    radnik["ime"]=random.choice(imena)
    radnik["prezime"]=random.choice(prezimena)
    radnik["satnica"]=round(random.uniform(4,6),2)
    radnici.append(radnik)
    
for radnik in radnici:
    radnik["tjedni_sati"]=random.randint(20,30)

    

print(radnici)
print("_"*20)
ntorke=[]
ukupna_isplata=0
for radnik in radnici:
    isplata=radnik["satnica"]*radnik["tjedni_sati"]
    ntorka=(radnik["ime"],radnik["prezime"],isplata)
    ntorke.append(ntorka)
    ukupna_isplata=ukupna_isplata+isplata
    prosjecna_isplata=ukupna_isplata/15
print(ntorke)


print("ukupna isplata je:",ukupna_isplata)
print("prosjecna isplataje:" ,prosjecna_isplata)
for radnik in radnici:
    isplata=radnik["satnica"]*radnik["tjedni_sati"]
    if isplata>prosjecna_isplata:
        print(radnik["ime"]+" "+radnik["prezime"])
    
input("")
    
