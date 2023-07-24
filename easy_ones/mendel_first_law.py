#k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
def mendel(k, m , n):
    total = k + m + n
    t = total*(total -1)
    prob_k = (k* (k-1)+ 2*(m* k) + 3/4*(m* (m-1)) + n*m +2*k*n)/t
    return(prob_k)
print(round(mendel(28,23,27), 5))