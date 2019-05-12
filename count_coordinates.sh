#!/bin/bash
fname=$1
wody=$(grep -c OW $fname)
POPC=$(grep -c POPC $fname)
CHL1=$(grep -c CHL1 $fname)
echo "Uzupelnijtopologie!"
echo "Liczba TIP3: $wody"
echo "Liczba POPC: $(($POPC/134))"
echo "Liczba CHL1: $(($CHL1/74))"
