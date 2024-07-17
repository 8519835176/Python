a=input("enter the string")
s_count=0
l_count=0
v_count=0
for i in a:
    if i=="\n":
        l_count+=1
print(l_count)
for i in a:
    if i==" ":
        s_count+=1
print(s_count)       

      
