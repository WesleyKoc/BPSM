#!/usr/bin/python

#Write a Python programme/script that will take any DNA sequence and translate it into protein using the translation table.
#What happens if the DNA sequence contains undetermined bases (e.g. N)?
#Can you generate a translation in all three "forward" frames (transcription is on the top strand, starting at base 1, 2, and 3)?
#Can you generate a translation in all three "reverse" frames (transcription is on the bottom strand, starting at base end, end-1, and end-2)?



#Here's a dict that stores a codon usage table for translation:
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def func():
    translated = []
    dna = input("Give any DNA sequence at least 3 bases long ")
    while True:
        if len(dna) >= 3:
            break
        else:
            print("Ur sequence is too short, give a longer one")
    codons = [dna[i:i+3] for i in range(0,len(dna), 3)]
    for c in codons:
        for triplet, protein in gencode.items():
            if c == triplet:
                translated.append(protein)
            else:
                pass
    translated_seq = "".join(translated)
    return(translated_seq)



if __name__=="__main__":
    result = func()
    print(result)






















