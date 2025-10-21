#!/usr/bin/python

dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

ex1 = dna[:62]
ex2 = dna[90:]
print(ex1+ex2)

codseq = ex1+ex2

codpercent = 100*(len(codseq)/len(dna))
print(codpercent)
