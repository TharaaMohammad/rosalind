#Positive integers n = month n≤100 and m = lifespan m≤20.
n = 3
m = 20
dic ={}
def fib(m , n):
    if n in dic:
        return dic[n]
    else:

        if n == 1 or n == 2:
            dic[n] = 1
        elif n <= m:
            dic[n] = fib(m, n-1)+ fib(m, n-2)
        else:
            s= 0
            for i in range(2, m+1):
                s += fib(m, n-i)
            dic[n] = s
    return dic[n]
print(fib(18,90))