l=[4,5,6,8,9,6,1,2,3,7]
m=l[0]
sm=l[1]
for i in range(0,len(l)-1):
    if(l[i] < l[i+1]):
        temp=l(i)
        l[i]= l[i+1]
        l[i+1] = temp
    
print(l)