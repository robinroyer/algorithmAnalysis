def bucket_sort(seq):
    biggest = 0
    for number in seq:
        if number > biggest:
            biggest = number
    buckets = []
    buckets.append([]) * (biggest / 10 + 1)
    for number in seq:
        buckets[number / 10].append(number)
    for index, bucket in enumerate(buckets):
        #Using quicksort to sort individual buckets
        buckets[index] = quicksort(bucket)
    new_list = [number for number in bucket for bucket in buckets]
    return new_list
