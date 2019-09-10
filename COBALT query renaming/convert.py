#------------------------------------------------------------------------------#
#Import SeqIO from Biopython package
from Bio import SeqIO

#Files to change
fasta_file = "laci_alignment.fa"
nexus_file = "phage_results.nex"
output_file = "corrected.nex"

#Create list of species names from COBALT Fasta file
names = []
with open(fasta_file, "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        new_name = record.description.split('|', 3)[2] #select only species
        new_name = new_name.strip() #remove extra whitespace
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

#Import SearchIO from Biopython package
from Bio import SearchIO

#Files to change
blast_xml_file = 'phage_blastx.xml'
blast_fasta_file = 'phage_resultsx.fa'

#Read in Blast XML
blast_result = SearchIO.read(blast_xml_file, 'blast-xml')

#Convert to Fasta
records = []
for hit in blast_result:
    records.append(hit[0].hit)
    SeqIO.write(records, blast_fasta_file, 'fasta')

#------------------------------------------------------------------------------#
