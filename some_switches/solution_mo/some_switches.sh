#! /bin/bash

# bash ./some_switches.sh

# https://stackoverflow.com/questions/314675/how-do-i-redirect-the-output-of-an-entire-shell-script-within-the-script-itself

door_cnt=${1:-10}
pass_cnt=${2:-10}
show_hist="$3"

[[ "$4" ]] && exec > $4

declare -a switches
for((i=1; i <= $door_cnt; i++)); do
    switches[$i]=0
done

for((i=1; i <= $pass_cnt; i++)); do
    for((j=i; j <= $door_cnt; j += i)); do
        switches[$j]=$(( switches[j] ^ 1 ))
    done

    if [[ "$show_hist" ]] ; then
        for((q=1; q <= $door_cnt; q++)); do
            [[ ${switches[$q]} -eq 0 ]] && op="X" || op="_"
            echo -n "$op "
        done
        echo ""
    fi
done

for((i=1; i <= $door_cnt; i++)); do
    [[ ${switches[$i]} -eq 0 ]] && op="closed" || op="open"
    echo "Switch $i is $op."
done