def RNA_to_DNAt(RNAseq):
    DNAseq = ""
    for i in RNAseq:
        if i == "U":
            DNAseq += "T"
        else:
            DNAseq += i
    return DNAseq
def DNA_Ptranscribe(DNAseq):
    codons = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    proteinseq = ""
    codon = ""
    for i in range(len(DNAseq))[::3]:
        codon = DNAseq[i:i+3]
        if codons[codon] != '_':
            proteinseq += codons[codon]
        elif codons == '_':
            break
    return proteinseq
input_data = open('C:\\Users\\Lenovo\\Downloads\\rosalind_prot.txt','r')
RNAseq = input_data.read().strip("\n")
DNAseq = RNA_to_DNAt(RNAseq)
proteinseq = DNA_Ptranscribe(DNAseq)
f= open("C:\\Users\\Lenovo\\Downloads\\Proteinseq.txt","w+")
f.write(proteinseq)
f.close()
input_data.close()
print(proteinseq)

