findParent =[7,3,5,1]
heightOfTheTree = 3

leafNodes = [1]
noOfTerms = len(leafNodes)
noOfExpectedTerms = noOfTerms*2
noOfPairs=noOfTerms/2
totalNoOfleafNodes = 2**(heightOfTheTree-1)
totalNoOfNodesInTheTree = (2**heightOfTheTree)-1
x=totalNoOfleafNodes
nodeTreeList = []
while(x!=1):
    totalNoOfNodesInTheTree = totalNoOfNodesInTheTree + (x/2)
    nodeTreeList.append(x)
    x=x/2
nodeTreeList.append(x)
while(noOfTerms<totalNoOfleafNodes):
    x = noOfExpectedTerms-1
    templist = []
    for i in leafNodes:
        templist.append(i+x)  
    for i in templist:
        leafNodes.append(i)
    noOfPairs=noOfTerms/2
    noOfTerms = len(leafNodes)
    noOfExpectedTerms = noOfTerms*2
perfectBinaryTree = []
for i in range (0,heightOfTheTree):
    templist=[]
    for j in range (0,nodeTreeList[0]):
        templist.append(0)
    perfectBinaryTree.append(templist)
for i in range(0,len(leafNodes)):
    perfectBinaryTree[heightOfTheTree-1][i]=leafNodes[i]
j=0
k=0
counter = 0
p=0
for i in range (heightOfTheTree-1,0,-1):
    while (j<nodeTreeList[k]):
        if (j%2!=0):
            perfectBinaryTree[i-1][p]=perfectBinaryTree[i][j]+1
            p=p+1
        j = j+1
    k = k+1
    p=0
    j=0
indexChildList = []
k=0
while (k<len(findParent)):
    for i in range (0,heightOfTheTree):
        if (k==len(findParent)):
            break
        for j in range (0,nodeTreeList[0]):
            templist=[]
            if (findParent[k]==perfectBinaryTree[i][j]):
                templist.append(i)
                templist.append(j)
                k = k+1
                indexChildList.append(templist)
                break
                


indexOfParent = []
ParentList=[]
for i in indexChildList:
    templist = []
    a=i[0]
    b=i[1]
    if (a==0):
        templist.append(-1)
        templist.append(-1)
        ParentList.append(-1)
    else:
        a = a-1
        b = int(b/2)
        templist.append(a)
        templist.append(b)
        ParentList.append(perfectBinaryTree[a][b])
    indexOfParent.append(templist)

return (ParentList)