n = 5
k = 1
#dp
dic = {}
def fib(n,k):
    if (n == 1 or n == 2)  and k >= 1:
        return 1
    else:
        if n-1 in dic:
            fibn_1 = dic[n-1]
        else:
            fibn_1 = fib(n-1, k)
            dic[n-1] = fibn_1
        if n-2 in dic:
            fibn_2 = dic[n-2]
        else:
            fibn_2 = fib(n-2, k)
            dic[n-2]= fibn_2
        return fibn_1+k*fibn_2
print(fib(n,k))

