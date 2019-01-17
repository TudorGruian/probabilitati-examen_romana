import pdftotext
import glob
titlu = 0
epic = 0
liric = 0
pastel = 0
doina = 0
mesaj = 0
basm = 0
nuvela = 0
schita = 0
fabula = 0
caracterizare = 0
balada = 0
filedir = glob.glob("tests/*.pdf")

for fil in filedir:
    with open(fil, 'rb') as f:
        text = pdftotext.PDF(f)[0]
        if "titlului" in text:
            print(fil[6:] + " titlu")
            titlu += 1 
        if "epic" in text:
            print(fil[6:] + " epic")
            epic += 1
        if "liric" in text:
            print(fil[6:] + " lirica")
            liric += 1
        if "pastel" in text:
            print(fil[6:] + " pastel")
            pastel += 1
        if "doina" in text:
            print(fil[6:] + " doina")
            doina += 1
        if "mesaj" in text:
            print(fil[6:] + " mesaj")
            mesaj += 1
        if "basm" in text:
            print(fil[6:] + " basm")
            basm += 1
        if "nuvel" in text:
            print(fil[6:] + " nuvela")
            nuvela += 1
        if "schi" in text:
            print(fil[6:] + " schita")
            schita += 1
        if "fabul" in text:
            print(fil[6:] + " fabula")
            fabula += 1
        if "caracterizare" in text:
            print(fil[6:] + " caracterizare personaj")
            caracterizare += 1
        if "balad" in text:
            print(fil[6:] + " balada")
            balada += 1

print("---------------------------------")

print("In decursul anilor s-a dat:")
print("Semn. titlu de " + str(titlu))
print("Epic de " + str(epic))
print("Liric de " + str(liric))
print("Pastel de " + str(pastel))
print("Doina de " + str(doina))
print("Mesaj de " + str(mesaj))
print("Basm de " + str(basm))
print("Nuvela de " + str(nuvela))
print("Schita de " + str(schita))
print("Fabula de " + str(fabula))
print("Caracterizare de " + str(caracterizare))
print("Balada de " + str(balada))
print("ori la toate*")

print("-------------------------------")

total = liric + epic + titlu + pastel + doina + mesaj + basm + nuvela + schita + fabula + caracterizare + doina
print("In total " + str(total))
print("La examen a picat liric " + str(100 * float(liric)/float(total)) + "%")
print("La examen a picat epic " + str(100 * float(epic)/float(total)) + "%")
print("La examen a picat titlu " + str(100 * float(titlu)/float(total)) + "%")
print("La examen a picat pastel " + str(100 * float(pastel)/float(total)) + "%")
print("La examen a picat doina " + str(100 * float(doina)/float(total)) + "%")
print("La examen a picat mesaj " + str(100 * float(mesaj)/float(total)) + "%")
print("La examen a picat basm " + str(100 * float(basm)/float(total)) + "%")
print("La examen a picat nuvela " + str(100 * float(nuvela)/float(total)) + "%")
print("La examen a picat schita " + str(100 * float(schita)/float(total)) + "%")
print("La examen a picat fabula " + str(100 * float(fabula)/float(total)) + "%")
print("La examen a picat caracterizare " + str(100 * float(caracterizare)/float(total)) + "%")
print("La examen a picat doina " + str(100 * float(doina)/float(total)) + "%")