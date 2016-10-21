from tri_insertion import triInsertion


"""
Implementation du Merge Sort en fonction du seuil

seq: le tableau contenant les données à trier
seuil: le seuil a partir duquel on applique un algorithme de tri par insertion sur un petit 
return: le tableau trié
"""
def triFusion(seq,seuil=1):
    n=len(seq)
    # Appel au tri par insertion en fonction du seuil
    if n<seuil+1 :
        return triInsertion(seq)
    # Appel recursif au tri fusion
    else :
        mid = n//2
        moitieGauche = seq[:mid]
        moitieDroite = seq[mid:]

        triFusion(moitieGauche,seuil)
        triFusion(moitieDroite,seuil)

        # Re-combinaise des solutions partielles en solution globale
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

