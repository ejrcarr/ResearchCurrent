from latin_squares import *
import numpy as np


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


def generateLatinCubesFromHigherSize(sizeOfCube):
    # arrayOfHigherSizedCubes = generateArrayOfLatinCubes(sizeOfCube)
    if(sizeOfCube == 4):
        file = open("LatinCubes/latinCubesSize4", "rb")
        arrayOfHigherSizedCubes = np.load(file, allow_pickle=True)
        arrayOfHigherSizedCubes = arrayOfHigherSizedCubes.tolist()
    else:
        arrayOfHigherSizedCubes = generateArrayOfLatinCubes(sizeOfCube)

    arrayofLowerSizedCubes = []
    for cube in arrayOfHigherSizedCubes:
        print(arrayOfHigherSizedCubes.index(cube))
        cube = list(cube)
        tempCube = []
        for square in cube[::-1]:
            tempSquare = []
            square = list(square)
            for row in square[::-1]:
                row = list(row)
                if row[0] != sizeOfCube:
                    print(square[::-1], "FIRST")
                    if row[sizeOfCube-1] != sizeOfCube:
                        indexOfFour = row.index(sizeOfCube)
                        row[indexOfFour] = row[sizeOfCube-1]
                        row.pop(sizeOfCube-1)
                    else:
                        row.remove(sizeOfCube)
                    if row not in tempSquare:
                        tempSquare.append(row)
                        print(tempSquare, "SECOND")
                    # print(tempSquare, "SECOND")
            if tempSquare not in tempCube:
                tempCube.append(tempSquare)
        if tempCube not in arrayofLowerSizedCubes:
            for squareExample in tempCube:
                if not isValidLatinSquare(squareExample):
                    print(squareExample, "CHECK HERE")

            arrayofLowerSizedCubes.append(tempCube)
    return arrayofLowerSizedCubes
