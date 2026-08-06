import random
import os

while True:
    try:
        passw = input("Wprowadź tekst do zaszyfrowania: ")
        if not passw.isalpha() or passw.isspace():
            continue
        break
    except:
        print("Złe dane")
    
def szyfruj(ciag):
    ind = []
    i = 0
    napis = []
    for x in ciag:
        ind.append(i)
        i += 1
        napis.append(x)
    random.shuffle(ind)
    o = 0
    szyfNapis = ""
    for n in ind:
        szyfNapis += napis[n]
    #print(szyfNapis)
    
    if os.path.exists("file.txt"):
        os.remove("file.txt")
    else:
        open("file.txt", "x")
    with open("file.txt", "w") as f:
        f.write(szyfNapis + "\n")
        for e in ind:
            f.write(str(e) + ",")
        f.close()
szyfruj(passw)
with open("file.txt", "r") as f:
    napis = f.readline()
    index = f.readline()
    print(napis)
def deszyfruj(n, i):
    inde = str(i)
    ind = inde.split(",")
    ind.pop(ind.__len__()-1)
    indTab = []
    for e in ind:
        indTab.append(int(e))
    tabDesz = ""
    for e in range(indTab.__len__()):
        tabDesz += napis[indTab.index(e)]
    print(f"Odszyfrowany tekst: {tabDesz}")
deszyfruj(napis, index)

