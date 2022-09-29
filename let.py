import random
import string 
fil1 = [] 
fil2 = [] 
fil3 = []
fil4 = [] 
ingrese = int(input("Ingrese la cantidad de lineas: ")) 
for i in range(ingrese): 
    fil1.append(random.randint(0,5000)) 
    fil2.append(random.choice(string.ascii_letters)) 
    fil3.append(random.randint(0,5000)) 
    fil4.append(random.randint(0,5000)) 
name = input("Ingrese el nombre del archivo: ")
doc = open(name,'w')
for j in range(ingrese): 
    doc.write('{}, {}, {}, {}\n'.format(fil1[j],fil2[j],fil3[j], fil4[j])) 
doc.close()
