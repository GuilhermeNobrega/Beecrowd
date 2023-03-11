'''x = input()
y = input()
z = input()

if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    a = 'aguia'

if x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    a = 'pomba'

if x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    a = 'homem'

if x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    a = 'vaca'

if x == 'invertebrado' and y == 'inseto' and z == 'hematofago':
    a = 'pulga'

if x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    a = 'lagarta'

if x == 'invertebrado' and y == 'anelideo' and z == 'hematofago':
    a = 'sanguessuga'

if x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    a = 'minhoca'

print(a)


c1=input()
c2=input()
c3=input()
if (c1=="vertebrado"):
    if (c2=="ave"):
        if(c3=="carnivoro"):
            print("aguia")
        elif(c3=="onivoro"):
            print("pomba")
    elif(c2=="mamifero"):
        if(c3=="onivoro"):
            print("homem")
        elif(c3=="herbivoro"):
            print("vaca")
elif(c1=="invertebrado"):
    if(c2=="inseto"):
        if(c3=="hematofago"):
            print("pulga")
        elif(c3=="herbivoro"):
            print("lagarta")
    elif(c2=="anelideo"):
        if(c3=="hematofago"):
            print("sanguessuga")
        elif(c3=="onivoro"):
            print("minhoca")'''

a = input()
b = input()
c = input()

if a== "vertebrado":
    if b=="ave":
        if c== "carnivoro":
            print('aguia')
        elif c=="onivoro":
            print('pomba')
    elif b== 'mamifero':
        if c=='onivoro':
            print('homem')
        if c=='herbivoro':
            print('vaca')

elif a=='invertebrado':
    if b=='inseto':
        if c =='hematofago':
            print('pulga')
        elif c =='herbivoro':
            print('lagarta')
    elif b=='anelideo':
        if c=='hematofago':
            print('sanguessuga')
        elif c=='onivoro':
            print('minhoca')
