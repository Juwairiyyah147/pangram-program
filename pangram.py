st=input("enter the string")
lst=[]
str=st.lower()
for ch in str:
    if ch in lst or ch== " ":
        continue
    else:
        lst.append(ch)



newl=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=0

for c in newl:
    if c in lst:
        continue
    else:
        b=1        
        break
        
if b==0:
    print("the given string is a pangram")

else:
    print("the given string is NOT a pangram")
    

       
