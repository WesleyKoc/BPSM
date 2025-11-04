#The code should allow user to:

#to identify a family of protein sequences from a user-defined subset of the taxonomic tree (e.g. glucose-6-phosphatase proteins from Aves (birds), or ABC transporters in mammals, or kinases in rodents, or adenyl cyclases in vertebrates etc.) that could then be processed using, for example, one or more of the EMBOSS programmes installed on the MSc server:

##to determine, and plot, the level of protein sequence conservation across the species within that taxonomic group

##to scan the protein sequence(s) of interest with motifs from the PROSITE database, to determine whether any known motifs (domains) are associated with this subset of sequences.



#The code needs to be generic:

#the user of your code will specify the protein family, and the taxonomic group, and then your code will need to obtain the relevant protein sequence data, and perform all subsequent analyses and outputs in the user's space on the MSc server.

##Do NOT set it up so it will only work in your workspace! As all files/databases/outputs will be made in the user's homespace on the MSc server, the user's allowable starting sequence set probably shouldn't have more than 1,000 sequences (note, this is just a guideline, not a hard limit!)

##How useful the programme will be might depend a bit on how many species are represented in the dataset chosen by the user (i.e. are the sequences all from one species, or are there many different species?), so it would probably make sense to tell the user, and give them the option to continue or not continue with the current dataset?

##There are almost certainly (many?) other checks that could/should be done at this stage before continuing to the main processing stages...

#to determine, and plot, the level of conservation between the protein sequences. Here we are wanting to establish the degree of similarity within the sequence set chosen. The output should go to screen and be saved as a file output.

##Think carefully about how many sequences you might want to use for the conservation analysis. We used a programme that does this sort of thing in the lectures, but this time, should you limit the number of sequences used for the conservation analysis and plotting to some number? If you think you should, working out which ones to keep could be done in several different ways, some a lot easier than others: the method of selection choice is up to you, should you go down this route.

#to scan protein sequence(s) of interest with motifs from the PROSITE database, to determine whether any known motifs (domains) are associated with this subset of sequences: were there any, and if so, what were their names?

#a "wildcard" option for you: to do any other appropriate EMBOSS (or other) analysis that you think might add relevant biological information to the outputs

##I am leaving it up to you to chose what might constitute "relevant biolgical information" that your programme will provide to the user: you are training to be a bioinformatician, so you should be able to decide, and justify your choice!

#maintain and provide for assessment a full git log history of your code writing/commit activities for this optional ICA


#Don't use Biopython

#Don't use a series of unix or bash scripts calling from python

#Make available as a passworded ccrypt encrypted file in a PUBLIC repository on GitHub in your Bxxxxxx-2025 GitHub account

#Some of the programs you might (or might not...!) need are, or should be, already installed:

##esearch, efetch, and others for searching and retrieving from any of the NCBI databases from the edirect package

##clustalo for clustering sequences etc

##makeblastdb, blastn, blastx, blastp for doing BLAST analyses etc

##plotcon and many others from EMBOSS ; use -help -verbose to get more info, or check out the link given above



#Consider the following:

#There can be quite a number of different ways to structure a solution. Remember, as you may have done for the optional ICA1 (and each set of exercise problems...), break up the main problem into smaller bits, figure those out, then put them all back together. Draw everything out schematically on paper first, so you know where everything should go/what might be needed both in terms of input and output.

#lots of comment lines in the code (please!)

#ALWAYS test the code with lots of print statements, you can comment them out later

#ALWAYS test the code with something that you know will work

#the user may be clever, but they can't read your mind: be explicit in telling them what they can and can't do, preferably at the time they are doing it, not aftwerwards...!

#have lots of "error traps" in your code (e.g. when the wrong thing is input, or there is no output, or ...)
##Remember: Use try except loop for error traps

#the code is fine, but there is no output on a different test set: what now? HELP!
























