def solution(map):
    widthOfTheMatrix = len(map[0])
    heightOfTheMatrix = len(map)
    print 'The width of the matrix is', widthOfTheMatrix
    print 'The width of the matrix is', heightOfTheMatrix

    def findPath():
        pass
        # added some nonsense


map = [[0, 1, 1, 0],[0, 0, 0, 1],[1, 1, 0, 0],[1, 1, 1, 0]]
availablePath = solution(map)
print 'Available Path :',availablePath