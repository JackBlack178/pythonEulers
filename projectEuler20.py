def factorial(n):
    if n==1:
        return 1

    else:
        return factorial(n-1)*n
summ = 0
for i in str(factorial(100)):
    summ += int(i)
print(summ)
