#Exercise 3
#You need to write a Python script/programme that will generate overlapping short segments from a long string (i.e. a sliding window approach); e.g. if your input sequence was
#abcdefghijk
#and the window size chosen was 6, and the offset was 1, then the segments would be :
#abcdef
#bcdefg
#cdefgh
#defghi
#efghij
#fghijk


#Using the protein-coding region from the AJ223353 NCBI sequence ('remote_exon01.fasta', or whatever you called it) that you generated while doing the exercises in the last lecture, write a Python programme that generates segments that are 30 bases long, with a window offset of 3.
#Modify your Python script/programme to print each sliding window segment to the screen.
#Modify your Python script/programme to print the percentage GC content of each sliding window segment and the sequence.
#Modify your Python script/programme to write out the individual segments in fasta format (i.e. with an informative fasta header) into individual fasta files.
#Modify your Python script/programme to write out the individual segments in fasta format (i.e. with an informative fasta header) into a single fasta file.
#Modify your Python script/programme to include the partial sliding window segments that we get at the end of the sequence.
#Note that all of the above 'modifications' could/should be part of a single Python script/programme! For example, you might find it easier to add processing step (a), ensure it is working properly then try adding (b), and so on.


AJ_coding_seq = open('AJex.txt').read()

window = 30
offset = 3

segment_start = list(range(0,len(AJ_coding_seq),offset))


