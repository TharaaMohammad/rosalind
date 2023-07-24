#read file
input_dna = open("C:\\Users\\Lenovo\\Downloads\\rosalind_revc.txt","r")
dna = input_dna.read()

translator = {"A":"T", "T":"A", "C":"G", "G":"C"}
reversed_dna = ""

##other solution
# for x in input_dna[::-1]:
#     reversed_dna += x
# print(reversed_dna)

n = len(dna)
for i in range(n):
    if i == 0:
        continue
    idx = n-1-i # i = n-1 ch = \n
    reversed_dna += translator[dna[idx]]

print(reversed_dna)
input_dna.close()

