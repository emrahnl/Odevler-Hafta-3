##3.ODEV: LISTE AYIKLAMA


file = open("Takimlar.txt", "r")

gs = open("gs.txt", "a+")
bjk = open("bjk.txt", "a+")
fb = open("fb.txt", "a+")

for line in file:
    if 'Galatasaray' in line:
        gs.write(line)
        
    if'Fenerbahce' in line:
        fb.write(line)

    if "Besiktas" in line:
        bjk.write(line)
        
        

gs.close()
fb.close()
bjk.close()



