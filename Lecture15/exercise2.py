#Exercise 2
#Modify the function from the previous exercise above so that it accepts a list of amino acid residues rather than a single one, and count these within the protein sequence.
#If no list is given, the function should return the percentage of hydrophobic amino acid residues (i.e. amino acids A, I, L, M, F, W, Y, V).
#Hint: To get this one to work, you'll have to go through the list of amino acid residues one at a time, generate the count for each one, and come up with a total count.


import os, sys

seqin = sys.argv[1]
base = sys.argv[2] if len(sys.argv) > 2 else ""

def func(seqin, base):
    total_percent = 0
    for i in range(len(base)):
        percent = (seqin.count(base[i])/len(seqin))
        total_percent += percent
    if base == "":
        alist = ["A", "I", "L", "M", "F","W", "Y","V"]
        percent = sum(seqin.count(a) for a in alist)/len(seqin)
        total_percent += percent
    total_percentage = total_percent *100
    return round(total_percentage)

output = func(seqin, base)
print(output)

assert round(func("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)




