#!/bin/bash

# Utilisation
# 
# tp.sh -a [bucket|bucketSeuil|merge|mergeSeuil] -e [path_vers_exemplaire]
# 
# Arguments optionnels :
# 
# -p Imprime les nombres triés
# -t Imprime le temps d’exécution

OPTIONS=""
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -a|--algo)
    ALGO="$2"
    shift
    ;;
    -e|--ex_path)
    EX_PATH="$2"
    shift
    ;;
    -p|--print|-t|--time)
    OPTIONS="${OPTIONS}${1} "
    ;;
    *)
        echo "Argument inconnu: ${1}"
        echo "Usage du script:"
        echo "./tp.sh -a [bucket|bucketSeuil|merge|mergeSeuil] -e path_vers_exemplaire [-t] [-p]"
        exit
    ;;
esac
shift
done

python3 ./src/$ALGO.py $EX_PATH $OPTIONS
