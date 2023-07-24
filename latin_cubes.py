from latin_squares import *

"""


This file is to store the functions relating to latin cubes including testing 
and generation.

To generate latin cubes, use the function: generateArrayOfLatinCubes(sizeOfSquare)
Replacing the parameter with the integer amount of the desired size of latin cubes
you want to generate.

e.g. 
    arrayOfLatinCubesSizeThree = generateArrayOfLatinCubes(3)

"""


def isValidLatinCube(cube):
    sizeOfCube = len(cube)
    for square in cube:
        if not isValidLatinSquare(square):
            return False
    currRow = []
    for columnIndex in range(sizeOfCube):
        for rowIndex in range(sizeOfCube):
            for cubeIndex in range(sizeOfCube):
                currRow.append(cube[cubeIndex][columnIndex][rowIndex])
            if(len(currRow) != len(set(currRow))):
                return False
            currRow = []
    return True


def generateArrayOfLatinCubes(sizeOfCube):
    if sizeOfCube == 0:
        return []
    elif sizeOfCube == 1:
        return [0]
    row = [i for i in range(1, sizeOfCube+1)]
    totalSum = sum(row)
    validSquares = generateArrayOfLatinSquares(sizeOfCube)
    generatedLatinCubes = []
    defaultCube = [[[0 for i in range(sizeOfCube)] for i in range(
        sizeOfCube)] for i in range(sizeOfCube)]
    currentLatinCube = defaultCube[:]
    n = sizeOfCube - 1
    dynamicArray = [0 for i in range(n+1)]
    MAX = len(validSquares)
    p = 0
    while dynamicArray[n] == 0:
        if(len(dynamicArray[:n]) == len(set(dynamicArray[:n]))):
            for i in range(sizeOfCube-1):
                currentLatinCube[i] = validSquares[dynamicArray[i]]
            newSquare = []
            newRow = []
            sumOfCurrentColumns = 0
            for columnIndex in range(sizeOfCube):
                for rowIndex in range(sizeOfCube):
                    for cubeIndex in range(sizeOfCube-1):
                        sumOfCurrentColumns += currentLatinCube[cubeIndex][columnIndex][rowIndex]
                    newRow.append(totalSum - sumOfCurrentColumns)
                    sumOfCurrentColumns = 0
                newSquare.append(newRow[:])
                newRow = []
            currentLatinCube[sizeOfCube - 1] = newSquare[:]
            if(isValidLatinCube(currentLatinCube)):
                generatedLatinCubes.append(currentLatinCube)
            currentLatinCube = defaultCube[:]
        dynamicArray[0] += 1
        while dynamicArray[p] == MAX:
            dynamicArray[p] = 0
            p += 1
            dynamicArray[p] += 1
            if dynamicArray[p] != MAX:
                p = 0
    return generatedLatinCubes


if __name__ == "__main__":
    print("Here you would call these functions to generate Latin Cubes of size N")
