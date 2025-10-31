#Write a Python programme/script that will split the genomic DNA into coding and non-coding parts, and write each of these sub-sequences to individual files AND two separate files (so that we also have one for coding sequences, and one for non-coding sequences)

#your programme/script should make sure that all sequences are in upper case and are DNA

#your fasta headers should include the length of the sequence

#your output fasta file names should, where possible, be the same as the fasta header, followed by the ".fasta" suffix, but not include any spaces: this is Linux, remember!

#your programme/script should include comments so that I/anyone can understand what you have done

#your programmes/scripts should be committed in your personal git repository and pushed to GitHub

import os
import sys

with open ("AJ223353_noheader.fasta") as AJ223353:
    AJ223353_opened = AJ223353.read().upper()
    AJ223353_onlyDNA = AJ223353_opened.replace("X","").replace("S","").replace("K","").replace("L","")
    intron1 = AJ223353_onlyDNA[:29]
    intron2 = AJ223353_onlyDNA[409:]
    exon = AJ223353_onlyDNA[29:409]

with open("AJintr.txt","w") as intr_AJ:
    intr_AJ.write(intron1 + intron2)

with open ("AJex.txt","w") as ex_AJ:
    ex_AJ.write(exon)

with open ("plain_genomic_seq.txt") as local_seq:
    local_seq_opened = local_seq.read().upper()
    local_seq_opened_onlyDNA = local_seq_opened.replace("X","").replace("S","").replace("K","").replace("L","")
    exon1 = local_seq_opened_onlyDNA[:62]
    exon2 = local_seq_opened_onlyDNA[90:]
    intron = local_seq_opened_onlyDNA[62:90]

with open("plain_genomic_seq_ex.txt","w") as ex_plain:
    ex_plain.write(exon1 + exon2)

with open ("plain_genomic_seq_intr.txt","w") as intr_plain:
    intr_plain.write(intron)
