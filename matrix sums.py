a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
r1=a[0][0]+a[0][1]+a[0][2]
r2=a[1][0]+a[1][1]+a[1][2]
r3=a[2][0]+a[2][1]+a[2][2]
c1=a[0][0]+a[1][0]+a[2][0]
c2=a[0][1]+a[1][1]+a[2][1]
c3=a[0][2]+a[1][2]+a[2][2]
d=a[0][0]+a[1][1]++a[2][2]
print("row 1 sum",r1)
print("row 2 sum",r2)
print("row 3 sum",r3)
print("column 1 sum",c1)
print("column 2 sum",c2)
print("column 3 sum",c3)
print("diagonal sum",d)
