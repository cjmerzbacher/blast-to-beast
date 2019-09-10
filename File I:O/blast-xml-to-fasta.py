#------------------------------------------------------------------------------#

#Import from Biopython package
from Bio import SearchIO, SeqIO

#Files to change
blast_xml_file = 'Sequence Files/phage-blastx-alignment-blosum62-gap15-2.xml'
blast_fasta_file = 'Sequence Files/phage_blastx-alignment-blosum62-gap15-2.fa'

#Read in Blast XML
blast_result = SearchIO.read(blast_xml_file, 'blast-xml')

#Convert to Fasta
records = []
for hit in blast_result:
    records.append(hit[0].hit)
    SeqIO.write(records, blast_fasta_file, 'fasta')

#------------------------------------------------------------------------------#
