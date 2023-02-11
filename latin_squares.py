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


def isValidReducedLatinSquare(square):
    import numpy as np

    rotated = np.array(square)
    validRow = [i for i in range(1, len(square) + 1)]

    return (validRow == square[0]) and (square[0] == rotated[:, 0]).any() and isValidLatinSquare(square)


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


def generateValidRows(row):
    import itertools
    return list(itertools.permutations(row))


def oldGenerateArrayOfLatinSquares(sizeOfSquare):
    if sizeOfSquare == 0:
        return []
    elif sizeOfSquare == 1:
        return [0]

    row = [i for i in range(1, sizeOfSquare+1)]
    totalSum = sum(row)
    validRows = generateValidRows(row)
    generatedLatinSquares = []
    defaultArray = [[0 for i in range(sizeOfSquare)]
                    for i in range(sizeOfSquare)]
    currentLatinSquare = defaultArray

    n = sizeOfSquare
    # n = sizeOfSquare - 1

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
    defaultArray = [[0 for i in range(sizeOfSquare)]
                    for i in range(sizeOfSquare)]
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
