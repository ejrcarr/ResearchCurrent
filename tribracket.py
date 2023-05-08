from latin_cubes import generateArrayOfLatinCubes, isValidLatinCube
from latin_squares import generateArrayOfLatinSquares
import numpy as np


def isValidTribracket(cube):
    if not isValidLatinCube(cube):
        return False

    N = np.array(cube)
    N = (N-1).tolist()

    rowLength = len(cube[0][0])
    for a in range(rowLength):
        for b in range(rowLength):
            for c in range(rowLength):
                for d in range(rowLength):

                    FAILS_FIRST_EQUATION = N[a][b][N[b][c][d]
                                                   ] != N[a][N[a][b][c]][N[N[a][b][c]][c][d]]
                    FAILS_SECOND_EQUATION = N[N[a][b][c]
                                              ][c][d] != N[N[a][b][N[b][c][d]]][N[b][c][d]][d]

                    if FAILS_FIRST_EQUATION or FAILS_SECOND_EQUATION:
                        return False
    return True


def isValidVirtualNAlgebra(cube, secondCube, square):
    if not isValidTribracket(cube):
        return False

    N = [[[0 for i in range(len(cube))] for i in range(len(cube))]
         for i in range(len(cube))]
    nTwo = [[[0 for i in range(len(secondCube))] for i in range(
        len(secondCube))] for i in range(len(secondCube))]
    latinSquare = [[0 for i in range(len(square))] for i in range(len(square))]

    for cubeIndex in range(len(cube)):
        for rowIndex in range(len(cube)):
            for columnIndex in range(len(cube)):
                N[cubeIndex][rowIndex][columnIndex] = cube[cubeIndex][rowIndex][columnIndex] - 1
                nTwo[cubeIndex][rowIndex][columnIndex] = cube[cubeIndex][rowIndex][columnIndex] - 1

    for row in range(len(square)):
        for column in range(len(square)):
            latinSquare[row][column] = square[row][column] - 1

    rowLength = len(cube[0][0])
    for a in range(rowLength):
        for b in range(rowLength):
            for c in range(rowLength):
                for d in range(rowLength):

                    FAILS_FIRST_EQUATION = N[a][b][N[b][c][d]
                                                   ] != N[a][N[a][b][c]][N[N[a][b][c]][c][d]]
                    FAILS_SECOND_EQUATION = N[N[a][b][c]
                                              ][c][d] != N[N[a][b][N[b][c][d]]][N[b][c][d]][d]

                    FAILS_THIRD_EQUATION = nTwo[a][nTwo[a][b][c]][c] != b
                    FAILS_FOURTH_EQUATION = nTwo[a][b][nTwo[b][c][d]
                                                       ] != nTwo[a][nTwo[a][b][c]][nTwo[nTwo[a][b][c]][c][d]]
                    FAILS_FIFTH_EQUATION = nTwo[nTwo[a][b][c]
                                                ][c][d] != nTwo[nTwo[a][b][nTwo[b][c][d]]][nTwo[b][c][d]][d]
                    FAILS_SIXTH_EQUATION = N[nTwo[a][b][c]][c][d] != nTwo[N[a]
                                                                          [b][nTwo[b][c][d]]][nTwo[b][c][d]][d]
                    FAILS_SEVENTH_EQUATION = N[a][b][nTwo[b][c][d]
                                                     ] != nTwo[a][nTwo[a][b][c]][N[nTwo[a][b][c]][c][d]]

                    FAILS_FIRST_SQUARE_BRACKET = N[a][latinSquare[a]
                                                      [b]][b] != latinSquare[a][b]
                    FAILS_SECOND_SQUARE_BRACKET = latinSquare[a][N[a]
                                                                 [b][c]] != N[a][b][latinSquare[b][c]]
                    FAILS_THIRD_SQUARE_BRACKET = N[a][b][c] != N[N[a]
                                                                 [b][latinSquare[b][c]]][latinSquare[b][c]][c]
                    FAILS_FOURTH_SQUARE_BRACKET = latinSquare[N[a]
                                                              [b][c]][c] != N[latinSquare[a][b]][b][c]
                    FAILS_FIFTH_SQUARE_BRACKET = N[a][b][c] != N[a][latinSquare[a]
                                                                    [b]][N[latinSquare[a][b]][b][c]]

                    FAILS_FIRST_ANGLE_BRACKET = latinSquare[a][nTwo[a]
                                                               [b][c]] != nTwo[a][b][latinSquare[b][c]]
                    FAILS_SECOND_ANGLE_BRACKET = nTwo[a][b][c] != nTwo[nTwo[a]
                                                                       [b][latinSquare[b][c]]][latinSquare[b][c]][c]
                    FAILS_THIRD_ANGLE_BRACKET = latinSquare[nTwo[a]
                                                            [b][c]][c] != nTwo[latinSquare[a][b]][b][c]
                    FAILS_FOURTH_ANGLE_BRACKET = nTwo[a][latinSquare[a]
                                                         [b]][nTwo[latinSquare[a][b]][b][c]] != nTwo[a][b][c]

                    if FAILS_FIRST_EQUATION or FAILS_SECOND_EQUATION or FAILS_THIRD_EQUATION or FAILS_FOURTH_EQUATION or FAILS_FIFTH_EQUATION or FAILS_SIXTH_EQUATION or FAILS_SEVENTH_EQUATION:
                        return False

                    if FAILS_FIRST_SQUARE_BRACKET or FAILS_SECOND_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET:
                        return False

                    if FAILS_FIRST_ANGLE_BRACKET or FAILS_SECOND_ANGLE_BRACKET or FAILS_THIRD_ANGLE_BRACKET or FAILS_FOURTH_ANGLE_BRACKET:
                        return False
    return True


def isValidPartialCube(cube):
    rowColLength = len(cube[0][0])
    for column in range(rowColLength):
        for row in range(rowColLength):
            for square in range(len(cube)-2):
                if cube[square][row][column] == cube[square+1][row][column]:
                    return False

    return True


def generateValidTribracketLatinCubes(sizeOfCube):
    # Edge cases
    if sizeOfCube == 0:
        return []
    elif sizeOfCube == 1:
        return [0]

    TOTAL_ROW_SUM = sum([i for i in range(1, sizeOfCube+1)])

    validSquares = generateArrayOfLatinSquares(sizeOfCube)
    generatedLatinCubes = []  # really tribrackets
    generatedCubes = []

    defaultCube = [[[0 for i in range(sizeOfCube)] for i in range(
        sizeOfCube)] for i in range(sizeOfCube)]

    currentLatinCube = defaultCube[:]
    n = sizeOfCube - 1
    dynamicArray = [0 for i in range(n+1)]

    MAX = len(validSquares)
    p = 0
    while dynamicArray[n] == 0:
        # print(dynamicArray[n-1]) #print to console progress
        if(len(dynamicArray[:n]) == len(set(dynamicArray[:n]))):
            for i in range(sizeOfCube-1):
                currentLatinCube[i] = validSquares[dynamicArray[i]]
            if isValidPartialCube(currentLatinCube):
                newSquare = []
                newRow = []
                sumOfCurrentColumns = 0
                for columnIndex in range(sizeOfCube):
                    for rowIndex in range(sizeOfCube):
                        for cubeIndex in range(sizeOfCube-1):
                            sumOfCurrentColumns += currentLatinCube[cubeIndex][columnIndex][rowIndex]
                        newRow.append(TOTAL_ROW_SUM - sumOfCurrentColumns)
                        sumOfCurrentColumns = 0
                    newSquare.append(newRow[:])
                    newRow = []
                currentLatinCube[sizeOfCube - 1] = newSquare[:]

            # print(currentLatinCube)
                if(isValidLatinCube(currentLatinCube)):
                    generatedCubes.append(currentLatinCube)
                if(isValidTribracket(currentLatinCube)):
                    generatedLatinCubes.append(currentLatinCube)
                currentLatinCube = defaultCube[:]

        dynamicArray[0] += 1

        while dynamicArray[p] == MAX:
            dynamicArray[p] = 0
            p += 1
            dynamicArray[p] += 1
            if dynamicArray[p] != MAX:
                p = 0

    # tribracketArray = np.array(generatedLatinCubes, dtype=object)
    # file = open("Tribrackets/tribracketCubesSizeFour", "wb")
    # np.save(file, tribracketArray)
    # file.close

    # cubeArray = np.array(generatedCubes, dtype=object)
    # file = open("LatinCubes/latinCubesSize4", "wb")
    # np.save(file, cubeArray)
    # file.close

    return generatedLatinCubes


def generateNAlgebrasSizeThree():
    listOfTribracketCubesSizeThree = generateValidTribracketLatinCubes(3)
    listOfLatinSquaresSizeThree = generateArrayOfLatinSquares(3)

    generatedNAlgebras = []
    for tribracket in listOfTribracketCubesSizeThree:
        for secondTribracket in listOfTribracketCubesSizeThree:
            for square in listOfLatinSquaresSizeThree:
                if(isValidVirtualNAlgebra(tribracket, secondTribracket, square)):
                    generatedNAlgebras.append(
                        [tribracket, secondTribracket, square])

    return generatedNAlgebras


def generateNAlgebrasSizeFour():
    from ast import literal_eval
    with open('LatinCubes/latinCubesSize4.txt') as f:
        arrayOfLatinCubesSizeFour = literal_eval(f.read())
    listOfLatinSquaresSizeFour = generateArrayOfLatinSquares(4)

    generatedNAlgebras = []
    for tribracket in arrayOfLatinCubesSizeFour:
        for secondTribracket in arrayOfLatinCubesSizeFour:
            # for square in listOfLatinSquaresSizeFour:
            if(isValidVirtualNAlgebra(tribracket, secondTribracket, 0)):
                print("ADDED")
                generatedNAlgebras.append([tribracket, secondTribracket, 0])

    return generatedNAlgebras


def getArrayOfTribracketsSizeN(size):
    hm = {3: 'Three', 4: 'Four'}
    file = open(f"Tribrackets/TribracketsSize{hm[size]}", "rb")
    arrayOfTribracketsSizeN = np.load(file, allow_pickle=True)
    arrayOfTribracketsSizeN = arrayOfTribracketsSizeN.tolist()
    return arrayOfTribracketsSizeN


def getArrayOfNAlgebrasSizeThree():
    file = open("Tribrackets/NAlgebrasSizeThree", "rb")
    arrayOfNAlgebrasSizeThree = np.load(file, allow_pickle=True)
    arrayOfNAlgebrasSizeThree = arrayOfNAlgebrasSizeThree.tolist()
    return arrayOfNAlgebrasSizeThree


def getArrayOfVirtualNAlgebrasSizeThree():
    file = open("Tribrackets/VirtualNAlgebrasSizeThree", "rb")
    arrayOfVirtualNAlgebrasSizeThree = np.load(file, allow_pickle=True)
    arrayOfVirtualNAlgebrasSizeThree = arrayOfVirtualNAlgebrasSizeThree.tolist()
    return arrayOfVirtualNAlgebrasSizeThree


if __name__ == "__main__":
    print(len(getArrayOfTribracketsSizeN(4)))
    # size4TribracketsArray = generateValidTribracketLatinCubes(4)

    # print(getArrayOfVirtualNAlgebrasSizeThree())
    # print(len(generateValidTribracketLatinCubes(2)))
    # print(generateValidTribracketLatinCubes(3))

    # backupArraySize4 = np.array(size4TribracketsArray, dtype=object)
    # file = open("Backups/tribracketsSizeFour", "wb")
    # np.save(file, backupArraySize4)
    # file.close
    # ----------------------------------------------------------------------
    # READING FROM FILES
    # ----------------------------------------------------------------------
    # file = open("LatinCubes/latinCubesSize4", "rb")
    # arrayOfCubesSize4 = np.load(file, allow_pickle=True)
    # arrayOfCubesSize4 = arrayOfCubesSize4.tolist()
    # print(len(arrayOfCubesSize4))
