def isValidRow(square): 
        for row in square:
            if not isValid(row):
                return False
        return True
    
def isValidColumn(square):
    # zip squared essentially makes the rows the columns and the columns the rows
    for col in zip(*square):
        if not isValid(col):
            return False
    return True

def isValid(array):
    for i in range(len(array)):
        if (array[i] > len(array)) or (array[i] < 0):
            return False
    return len(array) == len(set(array))

def isValidLatinSquare(square): 
    return isValidRow(square) and isValidColumn(square)
            

def createLatinSquare(sizeOfSquare, firstElement):

    '''
    row = [i for i in range(1, sizeOfSquare+1)]

    # If firstElement != 1 then rotate current row to make firstElement the number 
    row = row[firstElement-1:] + row[:firstElement-1]
    return [row[i:] + row[:i] for i in range(sizeOfSquare)]

    # READABILITY
    # --------------------------------------
    # latinSquare = []
    # for i in range(sizeOfSquare):
    #     rotatedRow = row[i:] + row[:i]
    #     latinSquare.append(rotatedRow)
    # return latinSquare
    # ---------------------------------------
    '''


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield list(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield list(pool[i] for i in indices[:r])
                break
        else:
            return

def generateValidRows(row):
    totalSum = sum(row)
    permutations(row, len(row) - 1)
    currSum = 0
    validRowsSizeNMinusOne = list(permutations(row, len(row) - 1))
    for i in validRowsSizeNMinusOne:
        for j in range(len(i)):
            currSum += i[j]
        i.append(totalSum-currSum)
        currSum = 0
    return validRowsSizeNMinusOne[:]
    



def oldGenerateArrayOfLatinSquares(sizeOfSquare):
    if sizeOfSquare == 0:
        return []
    elif sizeOfSquare == 1:
        return [0]
    
    row = [i for i in range(1, sizeOfSquare+1)]
    totalSum = sum(row)
    validRows = generateValidRows(row)
    generatedLatinSquares = []
    defaultArray = [[0 for i in range(sizeOfSquare)] for i in range(sizeOfSquare)]
    currentLatinSquare = defaultArray

    n = sizeOfSquare

    dynamicArray = [0 for i in range(n+1)]

    MAX = len(validRows)
    p = 0
    while dynamicArray[n] == 0:

        if(len(dynamicArray[:n]) == len(set(dynamicArray[:n]))):
            for i in range(sizeOfSquare):
                currentLatinSquare[i] = validRows[dynamicArray[i]]

            if(isValidLatinSquare(currentLatinSquare)):
                generatedLatinSquares.append(currentLatinSquare)
            currentLatinSquare = defaultArray
    
        dynamicArray[0] += 1

        while dynamicArray[p] == MAX:
            dynamicArray[p] = 0
            p += 1
            dynamicArray[p] += 1
            if dynamicArray[p] != MAX:
                p = 0

    return generatedLatinSquares

def generateArrayOfLatinSquares(sizeOfSquare):
    if sizeOfSquare == 0:
        return []
    elif sizeOfSquare == 1:
        return [0]
    
    row = [i for i in range(1, sizeOfSquare+1)]
    totalSum = sum(row)
    validRows = generateValidRows(row)
    generatedLatinSquares = []
    defaultArray = [[0 for i in range(sizeOfSquare)] for i in range(sizeOfSquare)]
    currentLatinSquare = defaultArray

    n = sizeOfSquare - 1

    dynamicArray = [0 for i in range(n+1)]


    MAX = len(validRows)
    p = 0

    while dynamicArray[n] == 0:

        if(len(dynamicArray[:n]) == len(set(dynamicArray[:n]))):
            for i in range(sizeOfSquare):
                currentLatinSquare[i] = validRows[dynamicArray[i]]

            newRow = []
            sumOfCurrentColumns = 0
            for column in range(sizeOfSquare):
                for row in range(sizeOfSquare-1):
                    sumOfCurrentColumns += currentLatinSquare[row][column]
                newRow.append(totalSum - sumOfCurrentColumns)
                sumOfCurrentColumns = 0
            currentLatinSquare[sizeOfSquare - 1] = tuple(newRow)

            copyOfCurrentLatinSquare = currentLatinSquare[:]
            if(isValidLatinSquare(currentLatinSquare)):
                generatedLatinSquares.append(copyOfCurrentLatinSquare)
            currentLatinSquare = defaultArray
    
        dynamicArray[0] += 1

        while dynamicArray[p] == MAX:
            dynamicArray[p] = 0
            p += 1
            dynamicArray[p] += 1
            if dynamicArray[p] != MAX:
                p = 0

    
    return generatedLatinSquares

# import time
# startTime = time.time()

# print(len(generateArrayOfLatinSquares(4)))

# executionTime = (time.time() - startTime)
# print('New execution time in seconds: ' + str(executionTime))