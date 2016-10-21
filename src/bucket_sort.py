from tri_insertion import triInsertion


"""
bucket_sortrecurs est une implementation de l'algoryithme recursif Bucket Sort

seq: le tableau contenant les données à trier
threshold: le seuil a partir duquel on applique un algorithme de tri par insertion sur un petit exemplaire
nbbucket: le nombre de bucket dans lesquels separer nos données
return: le tableau trié
"""
def bucket_sortrecurs(seq,threshold,nbbucket=0):
    #  Valeur par default du nombre de bucket
    if nbbucket==0 :
        nbbucket=len(seq)

    biggest = seq[0]
    lowest = seq[0]

    for number in seq:
        if number < lowest :
            lowest = number
        if number > biggest:
            biggest = number
    # conditions de sortie 
    if biggest == lowest :
        return seq

    buckets = []
    for j in range (nbbucket) :
        buckets.append([])
    for number in seq:
        buckets[int((number-lowest)* (nbbucket-1) / (biggest - lowest ) )].append(int(number))
    for j in range(len(buckets)) :
        # appel recursif a bucket_sortrecurs
        if len(buckets[j])>threshold :
            buckets[j]=bucket_sortrecurs(buckets[j],threshold,nbbucket=0)
        # Tri via un tri insertion en fonction de notre seuil pour un bucket
        elif len(buckets[j])>1 :
            buckets[j]=triInsertion(buckets[j])
    
    # Re-cobinaison des solutions partielles en solution globale 
    new_list = []
    for bucket in buckets :
        for number in bucket :
            new_list.append(int(number))

    return new_list
