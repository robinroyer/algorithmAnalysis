from tri_insertion import triInsertion


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