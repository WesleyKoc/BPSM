#!/usr/bin/python

#Exercise 3
#Write a Python function that will take a DNA sequence along with an optional threshold and return True or False to indicate whether the DNA sequence contains a high proportion of undetermined bases (i.e not A, T, G or C).



def counter(sequence, threshold):
    seq_len = len(sequence)
    
    true_bases = ["A", "T", "G", "C"]
    total_base_freq = 0
    for i in true_bases:
        base_count = sequence.upper().count(i)
        total_base_freq = total_base_freq + base_count

    undetermined_bases = seq_len - total_base_freq
    proportion = (undetermined_bases/seq_len)

    if proportion > threshold:
        return True
    elif threshold == "" and proportion > 0.5:
        return True
    else:
        return False



dna = counter('ATTGTCGTTGTCGTTGTCGTTGTCGTTGTCG', 0.15)
print(dna)






