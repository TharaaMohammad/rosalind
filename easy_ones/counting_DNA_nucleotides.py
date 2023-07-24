input_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
count = {}
count["A"] = 0
count["C"] = 0
count["G"] = 0
count["T"] = 0
for n in input_dna:
    count[n]+=1
print(*count.values())
