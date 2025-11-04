#Exercise 1
#Write a Python function that takes two arguments (a protein sequence and an amino acid residue code) and returns the percentage of the protein that the amino acid makes up.

import os, sys

seqin = sys.argv[1]
base = sys.argv[2]

def func(seqin, base):
    percent = (seqin.count(base)/len(seqin))*100
    return round(percent)

output = func(seqin, base)
print(output)

assert round(func("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)







