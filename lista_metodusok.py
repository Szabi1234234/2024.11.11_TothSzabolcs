nyelvek = ["python " "python " "C " "C++ " "java"]

# változóhoz mentve megtartja a az eredeti listat is
nyelvek2 = sorted(nyelvek)

#sorbarendezi a listat- helyben rendezi
nyelvek.sort()
print(nyelvek)

#forditott sorrendbe rendezi a listat 
nyelvek.reverse()
print(nyelvek)

 # az adott elem első előfordulásának indexe
print(nyelvek.index("C "))

# az adott elem hányszor fordul elő
print(nyelvek.count('python'))

# NEM listametodus de igy lehet eldonteni hogy egy elemet tartalmaz e a lista
print('C++' in nyelvek)

nev = "Hello"
print(nev.index("l"))
