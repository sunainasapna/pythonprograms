l=[44,55,11,66,77,99,33,22,88]
print(l)
for i in range(0,len(l)-1):
    for j in range(0,len(l)-1):
        if(l[j]>l[j+1]):
            temp=l[j]
            l[j]= l[j+1]
            l[j+1] = temp
    print(l)
    
