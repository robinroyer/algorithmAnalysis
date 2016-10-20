def triInsertion(seq):
    for i in range(len(seq)):
        x=seq[i]
        j=i
        while (j>0 and seq[j-1]>x) :
            seq[j]=seq[j-1]
            j=j-1
        seq[j]=x
    return seq