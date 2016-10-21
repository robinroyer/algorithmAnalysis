# AlgorithmAnalysis

This repo is used to make an hybrid analysis of two recursive algorithms(empirical & theoretical):
- *Merge Sort*
- *Bucket Sort*

> Both of these two algorithms use the insertion Sort to sort small arrays depending on a threshold parameter.

### Execution

```bash
./tp.sh -a [bucket|bucketSeuil|merge|mergeSeuil] -e path_to_data_to_sort [-t] [-p]
# -t show execution time
# -p print the sorted result
```

> There are 180 different data files in the folder `./data` containing from `1000` to `500000` numbers.


### Report

A french report can be found at the root of this projet and will not be translate in the futur.
