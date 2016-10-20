import math
import numpy as np
import time
import sys

data=[[],[],[],[],[]]
scope= [1000,5000,10000,50000,100000]

for j in range(10) :
	for i in scope :
		read=open('data/testset_'+str(i)+'_2'+str(j)+'.txt','r')
		extracted_data=[]
		for line in read :
			extracted_data.append(int(line))
		read.close()
		data[scope.index(i)].append(extracted_data)

def triInsertion(seq):
    for i in range(len(seq)):
        x=seq[i]
        j=i
        while (j>0 and seq[j-1]>x) :
            seq[j]=seq[j-1]
            j=j-1
        seq[j]=x
    return seq
    
def bucket_sortrecurs(seq,threshold,nbbucket=0):
    if nbbucket==0 :
        nbbucket=len(seq)
    biggest = seq[0]
    lowest = seq[0]
    for number in seq:
        if number < lowest :
            lowest = number
        if number > biggest:
            biggest = number
    if biggest == lowest :
        return seq
    buckets = []
    for j in range (nbbucket) :
        buckets.append([])
    for number in seq:
        buckets[int((number-lowest)* (nbbucket-1) / (biggest - lowest ) )].append(int(number))
    for j in range(len(buckets)) :
        if len(buckets[j])>threshold :
            buckets[j]=bucket_sortrecurs(buckets[j],threshold)
        elif len(buckets[j])>1 :
            buckets[j]=triInsertion(buckets[j])
        
    new_list = []
    for bucket in buckets :
        for number in bucket :
            new_list.append(int(number))
    return new_list

def triFusion(seq,seuil=1):
    n=len(seq)
    if n<seuil+1 :
        return triInsertion(seq)
    else :
        mid = n//2
        moitieGauche = seq[:mid]
        moitieDroite = seq[mid:]

        triFusion(moitieGauche)
        triFusion(moitieDroite)

        i=0
        j=0
        k=0
        while i < len(moitieGauche) and j < len(moitieDroite):
            if moitieGauche[i] < moitieDroite[j]:
                seq[k]=moitieGauche[i]
                i=i+1
            else:
                seq[k]=moitieDroite[j]
                j=j+1
            k=k+1

        while i < len(moitieGauche):
            seq[k]=moitieGauche[i]
            i=i+1
            k=k+1

        while j < len(moitieDroite):
            seq[k]=moitieDroite[j]
            j=j+1
            k=k+1
    return seq
    
    
def whatsidealthreshold(sortf,seq):
	timer=[]
	testedthreshold=np.arange(1,100,5)
	for k in range (len(testedthreshold)):
		timer.append(0)
		for j in range(len(seq)):
			t1= time.time()
			sortf(seq[j],testedthreshold[k])
			t2=time.time()
			timer[k]+=t2-t1
	meantimer = [x / len(seq) for x in timer]
	fichier = open("./collected_data/moyennebucket"+str(len(seq[0]))+"_20.txt", "w")
	fichier.write('best threshold : '+str(testedthreshold[timer.index(min(timer))])+', min meantime : '+ str(min(meantimer))+',meantime for thrshold=0 : '+str(meantimer[0]))
	fichier.close()
	for x in meantimer :
		fichier = open("./collected_data/moyennebucket"+str(len(seq[0]))+"_20.txt", "a")
		fichier.write("\n"+str(x))
		fichier.close()
for j in range(len(data)):
	whatsidealthreshold(bucket_sortrecurs,data[j])
