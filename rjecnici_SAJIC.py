import random
imena=['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']
rijecnik={}
a=0
b=0
for ime in imena:
    if ime not in rijecnik:
        rijecnik[ime]=random.randint(1,5)
for ime in rijecnik:
    if rijecnik[ime]>1:
        a+=rijecnik[ime]
        b+=1
print("postotak prolaznosti je", a/b)
    
        
