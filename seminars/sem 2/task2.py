n, start = map(int, input().split())
curr, i = start, 1
while i < n:
    curr = curr ^ (start + 2*i)  
    i+=1
print(curr)