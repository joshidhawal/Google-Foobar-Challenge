def solution(x, y):
    # Your code here
    returnString=''
    
    requiredm=int(x)
    requiredf=int(y)
    
    m=requiredm
    f=requiredf
    generation=0
    
    '''if ((m==1 and f==2) or (m==2 and f==1)):
        generation=1
        returnString=str(generation)
        return returnString'''

    while(m>1 or f>1):
        greatorNumber = 0
        if (m>f):
            greatorNumber=m
            m=greatorNumber-f
        else:
            greatorNumber=f
            f=greatorNumber-m
        generation+=1
        if(m<1 or f<1):
            generation=0
            break
    
    if generation==0:
        returnString='impossible'
    else:
        returnString=str(generation)
    
    return returnString

x=2
y=1
result = solution(x,y)
print result