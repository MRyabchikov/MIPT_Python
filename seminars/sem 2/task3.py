n = int(input())
i, summa = 1, 0
while i <= n:
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        summa+=i
    i+=1
print(summa)