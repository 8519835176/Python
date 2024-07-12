a=[[1,1],[2,2]]
b=[[3,3],[4,4]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]


print(c)
