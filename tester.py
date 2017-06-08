classCount = [ 2,3,4,5,10 ]

for item in classCount:
    i = 0
    while (i+item)<20:
        i+=item
        print(i)
        if(i==item*2):
            break

numOfPointsRadiusList = [[8,3],[16,3],[16,4],[32,4],[32,5],[64,5],[64,6]]

for x, kVal in numOfPointsRadiusList:
    print(x,kVal)