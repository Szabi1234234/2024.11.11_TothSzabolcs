"""1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az
adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás
 mellé vesszővel elválasztva a lista által tartalmazott színeket!"""
#ha a szin nem szerepel a listában egészitsd ki a listat szinnel majd printeld is ki azt

"""szinek = ['piros', 'kek', 'zold', 'fekete', 'feher', 'sarga']

megadott_szin = input("Mondj egy szint! ")
if megadott_szin in szinek:

    print(f"A megadott szin , {megadott_szin} szerepel a listában")
else:

    print(f"A megadott szin , {megadott_szin} NEM szerepela a listában")
    szinek.append(megadott_szin)
    print(szinek)"""


# torold a megadott szint a listabol

szinek = ['piros', 'kek', 'zold', 'fekete', 'feher', 'sarga']

megadott_szin = input("Mondj egy szint! ")
if megadott_szin in szinek:

    print(f"A megadott szin , {megadott_szin} szerepel a listában")
    szinek.remove(megadott_szin)
    print(szinek)
else:

    print(f"A megadott szin , {megadott_szin} NEM szerepela a listában")
    szinek.append(megadott_szin)
    print(szinek)
