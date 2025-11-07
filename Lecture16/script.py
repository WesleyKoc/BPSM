#!/usr/bin/python

dna = "AATGATGAACGAC"
dinucleotides = []
for first in 'ATGC':
    for second in 'ATGC':
        dinucleotides.append(str(first) + str(second))

print(dinucleotides)



nonzero_counts = {}
