def solution(x, y):
    # Your code here
    returnString=''
    
    requiredm=long(x)
    requiredf=long(y)
    
    m=requiredm
    f=requiredf
    generation=long(0)
    
    while(m>1 or f>1):
        if(m==1 and f>m):
            generation=generation+(f-m)
            break
        elif(m>f and f==1):
            generation=generation+(m-f)
            break
        if (m>f):
            m=m-f
        else:
            f=f-m
        generation+=1
        #print 'm:',m,'f:',f
        if(m<1 or f<1):
            generation=0
            break
    if generation==0:
        returnString='impossible'
    else:
        returnString=str(generation)
    
    return returnString

x='100000000000000000000000000000000000000000000000000000000'
y='999999999999'
result = solution(x,y)
print result