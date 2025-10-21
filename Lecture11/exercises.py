#!/usr/bin/python

#Q1
dna1 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
adenine_count = dna1.count("A")
thymine_count = dna1.count("T")
dna1_length = len(dna1)
print(float((adenine_count + thymine_count)/dna1_length))

#Q2
dna2 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
rev_dna2 = dna2[::-1]
rev_comp_dna2 = ""
for x in rev_dna2:
    if x == "A":
        rev_comp_dna2 += "T"
    elif x == "T":
        rev_comp_dna2 += "A"
    elif x == "G":
        rev_comp_dna2 += "C"
    elif x == "C":
        rev_comp_dna2 += "G"
print(rev_comp_dna2)

#Q3
dna3 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
cut_5prime = dna3.find("GAATTC")
cut_3prime = dna3.find("AATTC")
frag1 = len(dna3[:cut_5prime])
frag2 = len(dna3[cut_3prime:])
print("The motif starts at position", int(cut_5prime)+1)
print("The cut site is between positions", int(cut_5prime)+1, "and", int(cut_3prime)+1)
print(frag2)
