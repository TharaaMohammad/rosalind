input_data = open('C:\\Users\\Lenovo\\Downloads\\rosalind_gc.txt','r')
dna = input_data.readlines()
dna_fasta ={}
#seperate the dna sequences:
for i in dna:
    if i.startswith(">"):
        seq_id = i[1:-1]
        dna_fasta[seq_id] = ""
    else:
        dna_fasta[seq_id] += i[:-1]
#calculate the GC content of each seq:
gc_dic ={}
for key in dna_fasta:
    total = 0
    gc_cont = 0
    for chr in dna_fasta[key]:
        if chr == "C" or chr == "G":
            gc_cont += 1
            total += 1
        else:
            total += 1
    gcper = gc_cont/total*100
    gc_dic[key]= gcper
#find the ID of the string with the highest GC-content:
max = 0
idmax = 0
for key in gc_dic:
    if gc_dic[key] >= max:
        max = gc_dic[key]
        idmax = key

print(f"{idmax} \n{max}")
input_data.close()


