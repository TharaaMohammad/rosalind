input_data = open("C:\\Users\\Lenovo\\Downloads\\rosalind_grph.txt", "r")
data = input_data.readlines()
dic_strings = {}
for line in data:
    if line.startswith(">"):
        ID = line.strip("\n").strip(">")
        dic_strings[ID] = ""
    else:
        dic_strings[ID] += line.strip('\n')
for key_1 in dic_strings:
    for key_2 in dic_strings:
        if key_1 != key_2:
            if dic_strings[key_1][-3:]== dic_strings[key_2][:3]:
                print(key_1, key_2)
                #print(dic_strings[key_1][-3:], dic_strings[key_2][:3])

input_data.close()
import numpy as np
a = np.zeros((4,4))
a[1][2] = 1
a[2][1] = 1

a[2][3] = 1
a[3][2] = 1

print(a)
