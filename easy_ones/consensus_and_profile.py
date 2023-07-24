# number of dna strings = i
# length = n
# DNA strings matrix Dij
# profile of occurrence Oxj
# reading fasta:
input_data = open('C:\\Users\\Lenovo\\Downloads\\rosalind_cons_2_dataset.txt','r')
# reading fasta:
FASTA = input_data.readlines()
stringID = ''
consensus_string = ''
max_num = 0
DNAstrings = {}
for i in range(len(FASTA)):
    if FASTA[i].startswith('>'):
        stringID = FASTA[i].strip("\n")
        DNAstrings[stringID] = ""
    else:
        DNAstrings[stringID] += FASTA[i].strip("\n")
# Building profile matrix
n = len(DNAstrings[stringID])
profile = {"A":[0]*n, "C":[0]*n, "G":[0]*n, "T":[0]*n}
for x in range(n):
    for key  in DNAstrings:
        dna_s = DNAstrings[key]
        ch = dna_s[x]
        profile[ch][x] += 1
# finding the consensus string
for j in range(n):
    max_num = 0
    max_nuc = ''
    for nuc in profile:
        if profile[nuc][j] > max_num:
            max_num = profile[nuc][j]
            max_nuc = nuc
        else: continue
    consensus_string += max_nuc

input_data.close()
print(consensus_string, "\nA: ", *profile['A'], "\nC: ", *profile['C'], "\nG: ", *profile['G'] , "\nT: ", *profile['T'] )
