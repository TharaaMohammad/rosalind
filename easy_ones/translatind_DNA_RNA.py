input_data = open('C:\\Users\\Lenovo\\Downloads\\rosalind_rna.txt','r')
RNA = ""
for i in input_data.read():
    if i == "T":
        RNA += "U"
        # print(RNA)
    else:
        RNA += i
print(RNA)
# print(input_data.read().replace("T", "U"))
input_data.close()