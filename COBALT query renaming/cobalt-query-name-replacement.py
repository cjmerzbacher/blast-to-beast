#------------------------------------------------------------------------------#
#Import SeqIO from Biopython package
from Bio import SeqIO

#Files to change
fasta_file = "Sequence Files/phage-cobalt-defaults-blastx-blosum62-gap15-2.fa"
nexus_file = "Sequence Files/phage-cobalt-defaults-blastx-blosum62-gap15-2-nexus.nex"
output_file = "Sequence Files/phage-cobalt-defaults-blastx-blostum62-gap15-2-nexus-corrected.nex"

#Create list of species names from COBALT Fasta file
names = []
with open(fasta_file, "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        new_name = record.description.split('|', 3)[2] #select only species
        new_name = new_name.strip()
        new_name = new_name.replace(" ", "-") #remove extra whitespace
        names.append(new_name)

#Replace query numbers with species names in a corrected file
with open(nexus_file, "r") as nexus, open(output_file, 'w') as corrected:
    new_records = []
    count = 0
    for record in SeqIO.parse(nexus, "nexus"):
        new_name = names[count]
        record.id = new_name
        new_records.append(record)
        count+=1
    SeqIO.write(new_records, corrected, 'nexus')

#------------------------------------------------------------------------------#
