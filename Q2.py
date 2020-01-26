'''
    Q2
'''
import random
import math

#main
#input
A = []
a = []

m= int(input("\n Enter m:"))
n= int(input("\n Enter n:"))

print("\n Enter Matrix:")
for i in range(0,m,1):
    a=[]
    print("\n Enter row {}".format(i))
    for j in range(0,n,1):
        a.append(random.randrange(0,100,1))
    A.append(a)

#print matrix
print("\n matrix:")
for i in range(0,m,1):
    for j in range(0,n,1):
        print(A[i][j],end=" ")
    print()

#calc sum
sum = 0
max=A[0][0]
for i in range(0,m,1):
    for j in range(0,n,1):
        sum+=A[i][j]
        if A[i][j]>max:
            max = A[i][j]


print("\n Sum is: {}".format(sum))
print("\n Max is: {}".format(max))


avg = sum/(m*n)         #4 elements in 2x2 matrix
print("\n Avg is: {}".format(avg))

a=[]

for i in range(0,m,1):
    for j in range(0,n,1):
        a.append(A[i][j])

#sort a
a.sort()

N=len(a)
print("\n no of elements in a: {}".format(N))

if(N%2==0):    #if((m*n)%2==0)      #no of elements is even
    x=a[int(N/2)-1]
    y=a[int(N/2 +1)-1]
    median = (x+y)/2
else:
    median = a[int((N+1)/2)-1]

print("\n Median: {}".format(median))
    

#finding mode
freq={}
for i in range(0,N,1):
    if (a[i] in freq): 
        freq[a[i]] += 1
    else: 
        freq[a[i]] = 1

max=0
for key, value in freq.items(): 
    if value>max:
        mode = key
        max=value
    print("% d : % d"%(key, value)) 


print("\n Mode: {}".format(mode))


#standard deviation
'''
    take a number
    subtract mean
    square
    add to sum

    at last divide sum by N-1
'''
sum=0
for i in range(0,N,1):
    val = a[i]-avg
    val = val*val
    sum+=val

std = math.sqrt(sum/(N-1))

print("\n Standard deviation: {}".format(std))

