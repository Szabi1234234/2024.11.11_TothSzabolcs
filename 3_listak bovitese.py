nyelvek = ["python " "python " "C " "C++ " "java"]


# a lista végére hozzáfűz egy elemet
nyelvek.append('Python')
   
# a listát másolja
nyelvek_masolat = nyelvek.copy()
   
# a lista végére hozzáfűz egy másik gyűjteményt (pl. listát)
nyelvek_honlapkesziteshez = ['HTML', 'CSS', 'JavaScript']
nyelvek.extend(nyelvek_honlapkesziteshez)
print(nyelvek)
   
# adott indexű helyre beszúrja a megadott elemet
nyelvek.insert(1, 'Go')   
print(nyelvek)  
print(len(nyelvek))
  


