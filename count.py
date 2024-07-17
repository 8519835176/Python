a=input("enter the string")
v_count=0
c_count=0
vowel=set("aeiou")
for i in a:
    if i in vowel:
        v_count+=1
    else:
         c_count+=1
print("vowels are",v_count)
print("consonents are",c_count)
