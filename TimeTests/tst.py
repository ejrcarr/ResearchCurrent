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
            
def generateValidRows(row):

    # If row is empty then there are no permutations
    if len(row) == 0:
        return []
 
    # If there is only one element in row then, only
    # one permutation is possible
    if len(row) == 1:
        return [row]
 
    # Find the permutations for row if there are
    # more than 1 characters
 
    currentPermutation = [] # empty list that will store current permutation
 
    # Iterate the input(row) and calculate the permutation
    for i in range(len(row)):
       m = row[i]
 
       # Extract row[i] or m from the list.  remrow is
       # remaining list
       remrow = row[:i] + row[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in generateValidRows(remrow):
           currentPermutation.append([m] + p)
    return currentPermutation


def generateArrayOfLatinSquaresComputingRow(sizeOfSquare):
    if sizeOfSquare == 0:
        return []
    elif sizeOfSquare == 1:
        return [0]

    row = [i for i in range(1, sizeOfSquare+1)]
    validRows = generateValidRows(row)
    generatedLatinSquares = []
    defaultArray = [[0 for i in range(sizeOfSquare)] for i in range(sizeOfSquare)]
    currentLatinSquare = defaultArray
    # How many loops do we need?
    n = sizeOfSquare
    dynamicArray = []
    for i in range(n+1):
        dynamicArray.append(0)
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



# arrayOfLatinSquaresSizeOne = generateArrayOfLatinSquaresComputingRow(1)
# arrayOfLatinSquaresSizeTwo = generateArrayOfLatinSquaresComputingRow(2)
# arrayOfLatinSquaresSizeThree = generateArrayOfLatinSquaresComputingRow(3)
# arrayOfLatinSquaresSizeFour = generateArrayOfLatinSquaresComputingRow(4)

# print(len(arrayOfLatinSquaresSizeOne))
# print(len(arrayOfLatinSquaresSizeTwo))
# print(len(arrayOfLatinSquaresSizeThree))
# print(len(arrayOfLatinSquaresSizeFour))



