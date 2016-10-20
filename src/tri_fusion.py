from tri_insertion import triInsertion

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

