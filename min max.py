#i    0          1        2
a= [[24,3,6],[8,12,18],[2,66,7]]
#j    0 1 2    0 1 2    0  1 2

nl=[]
max_=a[0][0]
min_=a[0][0]


for i in range (len(a)):
    for j in range(len( a[i])):
        if a[i][j]%2==0 and a[i][j]%3==0:
            nl.append(a[i][j])

        if a[i][j] > max_:
            max_=a[i][j]

        if a[i][j]<min_:
            min_=a[i][j]

print(nl)
print("maximum",max_)
print("minimum",min_)
