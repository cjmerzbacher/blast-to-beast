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
