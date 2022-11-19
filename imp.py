"""Lista
lista =[...]
lista=[10, 12, 3, 65]
lista[0] / elso= lista[0] => ez a 10 lesz

hossz:
len(lista) => 4
utolso= lista[3] / utolso= lista[len (lista) -1]

új elem hozzáadása:
lista.append(9)
    megváltozik a lista hossza

lista bejárása:
    számlálós ciklussal
        ciklusváltozó i=0
            while i < len(lista):
            i +=1
"""
"""
Harmadik feladat:
3. feladat
Adott egy lista, mely október havi napi középhőmérséklet értékeket tartalmazza.
homerseklet= [0,12,13,9,2,7].

Az első érték október 1.  
A program írja ki, melyik napon csökkent az előző naphoz képest  a 
hőmérséklet több, mint 3 fokot? 

A rendelkezésre álló idő 10 perc. 

A kódról és a program futásáról is képernyőképet kérek feltölteni. 
"""
homerseklet= [0, 12, 13, 9, 2, 7]
i = 0
while i < len(homerseklet) -1:
    if(homerseklet[i] - homerseklet[i+1] > 3):
        print(f"{i + 2}. napon ")
    i += 1

"""Az első olyan napot írja ki, amikor 3-mal csökkent a hőmérséklet"""

i = 0
while(i < len(homerseklet) - 1) and (homerseklet[1] - homerseklet[i+ 1] <= 3):
    i += 1
if (i < len(homerseklet) - 1):
    print(f"{i + 2}. napra ")
else:
    print(f"Nincs ilyen nap!")

"""
GitHub mire jó?
1. verziókövetés
2. csoportmunka segítése
3. 
"""

"""
git init => git mappa = repository (repo)
"""