DNA_string = open("C:\\Users\\Lenovo\\Downloads\\rosalind_hamm_1_dataset.txt", "r")
sequences = DNA_string.readlines()
seq1 = sequences[0]
seq2 = sequences[1]
def hamming_distance(s1, s2):
    dis = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dis += 1
    return dis
print(hamming_distance(seq1,seq2))
DNA_string.close()