#locations of t as a substring of s
input_data = open('C:\\Users\\Lenovo\\Downloads\\rosalind_subs_1_dataset.txt','r')
t = input_data.readline()
s = input_data.readline().strip("\n")
locations = []
motif =""
for i in range(len(t)- len(s)+1):
    motif = t[i:i+len(s)]
    if s == motif:
        locations.append(i+1)
print(*locations)
input_data.close()