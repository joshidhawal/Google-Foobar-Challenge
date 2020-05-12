listOfPlates = [3, 1, 4, 1, 5, 9]
numberOfPlates = len(listOfPlates)

listOfPlates=sorted(listOfPlates,reverse=True)
print 'list of Plates',listOfPlates
# Creating the Max possible number from these elements
maxPossibleNumber = 0
for i in listOfPlates:
    maxPossibleNumber = maxPossibleNumber + i
    maxPossibleNumber = maxPossibleNumber * 10
maxPossibleNumber = maxPossibleNumber/10
print 'Max Possible Number',maxPossibleNumber



def createListFromNumber(number):
    numberList=[]
    while (number>10):
        temp= number%10
        numberList.append(temp)
        number = number/10
    numberList.append(number)
    return numberList

# Check if the set of the numbers
def checkList(elementList,numberList):
    counter = 0
    for i in numberList:
        try:
            indexOfi = elementList.index(i)
            elementList.remove(i)
            counter +=1
        except Exception as e:
            return False
    return True
    

maxNumber = 0
counter = 0
listMaxNumber=[]


def findNumber(number,listOfPlates):
    numberList = createListFromNumber(number)
    status = checkList(listOfPlates,numberList)
    return status


for i in range(maxPossibleNumber,0,-1):
    status = findNumber(i,listOfPlates)
    try:
        if status:
            if i%3==0:
                print i
                break
    except Exception as e:
        print e
