n = 5
for i in range(n):
   print(' '*(n-i-1) + '*'*((2*i)+1) )
# resize top diamond
for i in range(n):
    print(' '*(i+0) + '*'*((2*((n-0)-i))-1))
# reposition bot diamond