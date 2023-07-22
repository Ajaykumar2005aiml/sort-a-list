b=[]
n=5
for i in range(1,n+1):
    value = (int(input("input")))
    if value > 0 :
      b.append(value)
    else:
      b.append(value)
      break
b.sort()
print(*b)
print("sum of elements: ",str(sum(b)))
