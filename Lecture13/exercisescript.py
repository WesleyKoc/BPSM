#Exercise 1
#The file input.txt contains a number of DNA sequences, one per line.
#Each sequence starts with the same 14 base pairs : these are from a sequencing adapter that should have been removed.

#Write a Python script/programme that will :
#(a) trim the adapter and write the 'cleaned' (adapter-free) sequences to a single new file AND
#(b) print the length of each adapter-free sequence to the screen.

input_content = open('input.txt').read().replace('ATTCGATTATAAGC','').split()
clean_sequences = open('clean_seq.txt', 'w')
for clean_lines in input_content:
    clean_sequences.write(clean_lines + '\n')
clean_sequences.close()



#Exercise 2
#The file genomic_dna2.txt contains a section of genomic DNA.
#The file exons.txt contains a list of start/stop positions of exons.
#Each exon is on a separate line and the start and stop positions are separated by a comma.

#Write a Python script/programme that will extract the exon segments, concatenate them, and write them to a new file.

genomic_dna2_read = open('genomic_dna2.txt').read().upper()
exons_read = open('exons.txt').read().rsplit()
with open('exon_cat', 'w') as exon_code:
    exon_code.write('Exercise 2 coding sequences\n\n')
    for exons in exons_read:
        startex = int(exons.split(',')[0])-1
        endex = int(exons.split(',')[1])
        exon_segment = genomic_dna2_read[startex : endex]
        exon_code.write(exon_segment)
exon_code.close()






#Exercise 4
#In the directory /localdisk/data/BPSM/Lecture13/ is a collection of files whose names end in .dna.
#Each file holds a collection of DNA sequences, one per line.
#What is required:
#Write a Python script/programme which creates nine new 'size range' directories, one for sequences between 100 and 199 bases long, one for sequences between 200 and 299 bases long, etc., etc..
#Choose any one of the .dna files as an input file, and write out each DNA sequence in that input file to a separate file in the appropriate 'size range' directory.




