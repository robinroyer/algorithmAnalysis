import time
import sys

# import our algorithm
from tri_fusion import triFusion
# safe sys.argv access
from get_argv import getArgv


# CONSTANTES
PRINT_TIME = "-t"
PRINT_LIST = "-p"

path = ""
option1 = ""
option2 = ""
options = ""

# le path de l'exemplaire considere
path = getArgv(1)
option1 = getArgv(2)
option2 = getArgv(3) 

options = option1 + option2
# tableau de nombre a trier
extracted_data=[]

# lecture du fichier contenant l'exemplaire
read=open(path,'r')
for line in read :
    extracted_data.append(int(line))
read.close()

# Execution du MergeSort
t1= time.time()
sorted_array = triFusion(extracted_data)
t2= time.time()

# Affichage du tri
if PRINT_LIST in options:
    print(" Les nombres triés sont : \r\n")
    for num in sorted_array:
        print(num)

# Affichage du temps d'execution
if PRINT_TIME in options:
    print(" Ce tri prend : ", t2 - t1, "secondes !\r\n")
