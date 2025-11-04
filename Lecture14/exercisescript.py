#data.csv contains some made-up data for a number of genes.
#Each line contains the following fields for a single gene in this order: species name, sequence, gene name, expression level.

#Exercise 1
#You need to write a Python programme/script that can:
#Print out the gene names for all genes from the species Drosophila melanogaster or Drosophila simulans.
#Print out the gene names for all genes that are between 90 and 110 bases long.
#Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200.
#Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster.
#For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65).
#hint: remember how we used a loop to read the contents of a file line-by-line in the last lecture...

with open(data.csv).read() as data:
    for line in data:
        gene_split = line.split(",")
        species = gene_split[0]
        seq = gene_split[1]
        gene_name = gene_split[2]
        exp_level = int(gene_split[3])
        AT_content = float((int(seq.count("A"))+int(seq.count("T")))/int(len(seq)))
        if species.startswith('Drosophila'):
            if AT_content>0.65:
                print("The gene is called" + gene_name + "and the AT content is high")
            elif AT_content<0.45:
                print("The gene is called" + gene_name + "and the AT content is low")
            else:
                print("The gene is called" + gene_name + "and the AT content is medium")
        if len(seq)>90 and len(seq)<110:
            if AT_content>0.65:
                print("The gene is called" + gene_name + "and the AT content is high")
            elif AT_content<0.45:
                print("The gene is called" + gene_name + "and the AT content is low")
            else:
                print("The gene is called" + gene_name + "and the AT content is medium")
        if AT_content<0.5 and exp_level>200:
            if AT_content>0.65:
                print("The gene is called" + gene_name + "and the AT content is high")
            elif AT_content<0.45:
                print("The gene is called" + gene_name + "and the AT content is low")
            else:
                print("The gene is called" + gene_name + "and the AT content is medium")
        if (gene_name.startswith('k') or gene_name.startswith('h')) and gene_name!="Drosophila melanogaster":
            if AT_content>0.65:
                print("The gene is called" + gene_name + "and the AT content is high")
            elif AT_content<0.45:
                print("The gene is called" + gene_name + "and the AT content is low")
            else:
                print("The gene is called" + gene_name + "and the AT content is medium")
data.close()



#Exercise 2: K-mer counting
#K-mers are short DNA subsequences with length "k" bases, and are usually generated using the "sliding window" method we used in the last lecture's exercise.

#Write a programme/script that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than some number of times n (you chose what the number n is!).

#For example, with
#dna="ATGCATCATG"
#k=2 # kmer size
#n=2 # more than this number found

#Sliding window with offset of 1 and with k=2 gives:
#AT
# TG 
#  GC 
#   CA
#    AT ... and so on


#so the result for this example should be AT because the kmers (k) are 2 bases long, and there are 3 instances of AT (n was 2, and 3 is more than 2).

#Neither CA nor TG get listed: they do appear twice each, but 2 is not more than 2....!

seqin = input("Provide a sequence:").upper()
try:
    if any(base not in "ATGC" for base in seqin):
        print("Give a valid DNA sequence")
except:
    pass

pos_kmer_sizes = list(range(2,int(len(seqin)-1)))

kmerfound_min = 3

for window in pos_kmer_sizes:
    kmersfound = []
    kmerrange = list(range(0,len(seqin)))
    for startbase in kmerrange:
        if (startbase+window) < len(seqin)+1:
            seqout = (seqin)[startbase:startbase+window]
            kmersfound = kmersfound + [seqout]
    nonredundantset = list(set(kmersfound))
    for kmerfrequencies in nonredundantset   :
       if kmersfound.count(kmerfrequencies) > kmerfound_min:
           print("Lots! " + str(kmerfrequencies)+" "+str(kmersfound.count(kmerfrequencies)))
       else   :
           print(str(kmerfrequencies) + " " + str(kmersfound.count(kmerfrequencies)))


#Exercise 3: Pairwise distances: how similar are two sequences?
#Here is a list of DNA sequences that are all equal in length, with varying degrees of similarity to each other:

#['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

#Write a programme/script that calculates and prints, for each pair of sequences, the percentage of identical positions (e.g. base #4 in seq 1 is the same as base #4 in seq 4, and so on).

#Hint:
#if base_in_seq1 == base_in_seq2:
#    do something









