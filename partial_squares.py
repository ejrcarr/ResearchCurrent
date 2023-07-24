from latin_squares import generateArrayOfLatinSquares
from virtual_tribracket import isValidVirtualNAlgebraTribracket, isVirtualTribracketTest
from tribracket import generateValidTribracketLatinCubes, isValidTribracket
import numpy as np


'''

[1, 2, 3]      [_, 2, 3]      [1, _, 3]       [1, 2, _]      [_, _, 3]     [1, _, _]     [_. 2, _]       [_, _, _]
[2, 3, 1]  --> [2, 3, 1]  --> [2. 3. 1]  -->  [2, 3, 1]  --> [2, 3, 1] --> [2, 3, 1] --> [2, 3, 1]  -->  [2, 3, 1]
[3, 1, 2]      [3, 1, 2]      [3, 1, 2]       [3, 1, 2]      [3, 1, 2]     [3, 1, 2]     [3, 1, 2]       [3, 1, 2]


[1, 2, 3]     [1, 2, 3]
[2, 3, 1] --> [_, _, _]   
[3, 1, 2]     [_, _, _]
                            -->    Duplicates
[1, 2, 3]     [1, 2, 3]
[3, 1, 2] --> [_, _, _]
[2, 3, 1]     [_, _, _]


'''


def generateArrayOfPartialSquares(sizeOfSquare):
    fullyDefinedSquares = generateArrayOfLatinSquares(sizeOfSquare)
    numberOfElements = sizeOfSquare * sizeOfSquare
    testArray = [fullyDefinedSquares] + [set()] * numberOfElements
    for i in range(len(testArray)-1):
        for square in testArray[i].copy():
            for row in range(len(square)):
                for col in range(len(square)):
                    newSquare = square[:]
                    newSquare = [list(line) for line in square]
                    if newSquare[row][col] != 1000:
                        newSquare[row][col] = 1000
                    else:
                        continue
                    newSquare = [tuple(line) for line in newSquare]
                    newSquare = tuple(newSquare)
                    testArray[i+1].add(newSquare)
    return testArray[-1]


def isNAlgebraTest(cube, square):

    cube = np.array(cube)
    cube = (cube - 1).tolist()
    square = np.array(square)
    square = (square - 1).tolist()

    rowLength = len(cube[0][0])
    for a in range(rowLength):
        for b in range(rowLength):
            for c in range(rowLength):

                '''

                1. [a, ab, b] = ab
                2. a[a, b, c] = [a, b, bc]
                3. [a, b, c] = [[a, b, bc], bc, c]
                4. [a, b, c]c = [ab, b, c]
                5. [a, b, c] = [a, ab, [ab, b, c]]

                [0, 0, 0, 0, 0] -> [0, 0, 1, 0, 1] -> [0,0, 1, 0, 2]

                '''

                ab = square[a][b]
                bc = square[b][c]
                abc = cube[a][b][c]

                if ab < 500:
                    aabb = cube[a][ab][b]
                    abCbCc = cube[ab][b][c]

                aabc = square[a][abc]

                if bc < 500:
                    aCbCbc = cube[a][b][bc]

                if (ab < 500):
                    FAILS_FIRST_SQUARE_BRACKET = aabb != ab
                else:
                    FAILS_FIRST_SQUARE_BRACKET = False

                if (aabc < 500 and bc < 500):
                    FAILS_SECOND_SQUARE_BRACKET = aabc != aCbCbc
                else:
                    FAILS_SECOND_SQUARE_BRACKET = False

                if (bc < 500):
                    FAILS_THIRD_SQUARE_BRACKET = abc != cube[aCbCbc][bc][c]
                else:
                    FAILS_THIRD_SQUARE_BRACKET = False

                if (square[abc][c] < 500 and ab < 500):
                    FAILS_FOURTH_SQUARE_BRACKET = square[abc][c] != abCbCc
                else:
                    FAILS_FOURTH_SQUARE_BRACKET = False

                if (ab < 500):
                    FAILS_FIFTH_SQUARE_BRACKET = abc != cube[a][ab][abCbCc]
                else:
                    FAILS_FIFTH_SQUARE_BRACKET = False

                # if(square[b][c] > 500 and (square[a][cube[a][b][c]] < 500 or square[cube[b][c][a]][a] < 500)):
                #     return False
                # if(square[b][c] < 500 and (square[a][cube[a][b][c]] > 500 or square[cube[b][c][a]][a] > 500)):
                #     return False
                if(square[b][c] > 500 and (square[a][cube[a][b][c]] < 500 and square[cube[b][c][a]][a] < 500)):
                    return False
                if(square[b][c] < 500 and (square[a][cube[a][b][c]] > 500 and square[cube[b][c][a]][a] > 500)):
                    return False

                if FAILS_FIRST_SQUARE_BRACKET or FAILS_SECOND_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET:
                    return False

    # If for-loops end then that means they are compatable.
    return True


def isVirtualNAlgebraPartial(secondCube, square):
    secondCube = np.array(secondCube)
    secondCube = (secondCube - 1).tolist()
    square = np.array(square)
    square = (square - 1).tolist()

    rowLength = len(secondCube[0][0])

    for a in range(rowLength):
        for b in range(rowLength):
            for c in range(rowLength):
                '''

                1. a{a, b, c} = {a, b, bc}
                2. {{a, b, bc}, bc, c} = {a, b, c}
                3. {a, b, c}c = {ab, b, c}
                4. {a, ab, {ab, b, c}} = {a, b, c}

                '''

                if(square[a][secondCube[a][b][c]] < 500) and (square[b][c] < 500):
                    FAILS_FIRST_ANGLE_BRACKET = square[a][secondCube[a]
                                                          [b][c]] != secondCube[a][b][square[b][c]]
                else:
                    FAILS_FIRST_ANGLE_BRACKET = False

                if(square[b][c] < 500):
                    FAILS_SECOND_ANGLE_BRACKET = secondCube[a][b][c] != secondCube[secondCube[a]
                                                                                   [b][square[b][c]]][square[b][c]][c]
                else:
                    FAILS_SECOND_ANGLE_BRACKET = False

                if(square[secondCube[a][b][c]][c] < 500) and (square[a][b] < 500):
                    FAILS_THIRD_ANGLE_BRACKET = square[secondCube[a]
                                                       [b][c]][c] != secondCube[square[a][b]][b][c]
                else:
                    FAILS_THIRD_ANGLE_BRACKET = False

                if(square[a][b] < 500):
                    FAILS_FOURTH_ANGLE_BRACKET = secondCube[a][square[a][b]
                                                               ][secondCube[square[a][b]][b][c]] != secondCube[a][b][c]
                else:
                    FAILS_FOURTH_ANGLE_BRACKET = False

                if FAILS_FIRST_ANGLE_BRACKET or FAILS_SECOND_ANGLE_BRACKET or FAILS_THIRD_ANGLE_BRACKET or FAILS_FOURTH_ANGLE_BRACKET:
                    return False

    return True


def generateVirtualNAlgebrasSizeThreePartials():
    # -----------------------------------------------------------------------------------
    # SIZE 3
    # -----------------------------------------------------------------------------------
    listOfTribracketCubesSizeThree = generateValidTribracketLatinCubes(3)
    listOfLatinSquaresSizeThree = generateArrayOfPartialSquares(3)

    generatedNAlgebras = []
    for tribracket in listOfTribracketCubesSizeThree:
        for secondTribracket in listOfTribracketCubesSizeThree:
            for square in listOfLatinSquaresSizeThree:
                if(isVirtualNAlgebraPartial(secondTribracket, square) and isNAlgebraTest(tribracket, square) and isVirtualTribracketTest(tribracket, secondTribracket)):
                    generatedNAlgebras.append(
                        [tribracket, secondTribracket, square])

    return generatedNAlgebras


def generateNAlgebraSizeThreePartials():
    # -----------------------------------------------------------------------------------
    # SIZE 3
    # -----------------------------------------------------------------------------------
    listOfTribracketCubesSizeThree = generateValidTribracketLatinCubes(3)
    listOfLatinSquaresSizeThree = generateArrayOfPartialSquares(3)

    generatedNAlgebras = []
    for tribracket in listOfTribracketCubesSizeThree:
        for square in listOfLatinSquaresSizeThree:
            if(isNAlgebraTest(tribracket, square)):
                generatedNAlgebras.append([tribracket, square])

    return generatedNAlgebras


def generateNAlgebraOrderNPartials(size):
    listOfTribracketCubes = generateValidTribracketLatinCubes(size)
    listOfLatinSquares = generateArrayOfPartialSquares(size)

    generatedNAlgebras = []
    for tribracket in listOfTribracketCubes:
        for square in listOfLatinSquares:
            if(isNAlgebraTest(tribracket, square)):
                generatedNAlgebras.append([tribracket, square])

    return generatedNAlgebras


def generateVirtualNAlgebrasOrderNPartials(size):
    listOfTribracketCubes = generateValidTribracketLatinCubes(size)
    listOfLatinSquares = generateArrayOfPartialSquares(size)

    generatedNAlgebras = []
    for tribracket in listOfTribracketCubes:
        for secondTribracket in listOfTribracketCubes:
            for square in listOfLatinSquares:
                if(isVirtualNAlgebraPartial(secondTribracket, square) and isNAlgebraTest(tribracket, square) and isVirtualTribracketTest(tribracket, secondTribracket)):
                    generatedNAlgebras.append(
                        [tribracket, secondTribracket, square])

    return generatedNAlgebras


def generateNAlgebraOrderNPartials(arrayOfTribrackets, arrayOfSquares):
    generatedNAlgebras = []
    for tribracket in arrayOfTribrackets:
        for square in arrayOfSquares:
            if(isNAlgebraTest(tribracket, square)):
                generatedNAlgebras.append([tribracket, square])

    return generatedNAlgebras


def generateVirtualNAlgebrasOrderNPartials(arrayOfTribrackets, arrayOfSquares):
    generatedNAlgebras = []
    for tribracket in arrayOfTribrackets:
        for secondTribracket in arrayOfTribrackets:
            for square in arrayOfSquares:
                if(isVirtualNAlgebraPartial(secondTribracket, square) and isNAlgebraTest(tribracket, square) and isVirtualTribracketTest(tribracket, secondTribracket)):
                    generatedNAlgebras.append(
                        [tribracket, secondTribracket, square])

    return generatedNAlgebras


# def generateNAlgebraSizeFourPartials():
#     # -----------------------------------------------------------------------------------
#     # SIZE 4
#     # -----------------------------------------------------------------------------------
#     listOfTribracketCubesSizeFour = generateValidTribracketLatinCubes(4)
#     file = open("Partials/partialSquaresSize4", "rb")
#     listOfLatinSquaresSizeFour = np.load(file, allow_pickle=True)
#     listOfLatinSquaresSizeFour = listOfLatinSquaresSizeFour.tolist()

#     generatedNAlgebras = []
#     for tribracket in listOfTribracketCubesSizeFour:
#         for square in listOfLatinSquaresSizeFour:
#             if(isNAlgebraTest(tribracket, square)):
#                 generatedNAlgebras.append([tribracket, square])

#     return generatedNAlgebras

# Uses backtracking to make all possible combinations of rows size n
def getAllPartialRows(n):
    result = []
    possibleValues = [1000] + [i+1 for i in range(n)]

    def backtrack(current_row, i):
        if len(current_row) == n:
            result.append(current_row[:])
            return
        if i >= n:
            return
        for num in possibleValues[:]:
            current_row.append(num)
            backtrack(current_row, i + 1)
            current_row.pop()
            backtrack(current_row, i + 1)
    backtrack([], 0)
    return result

# same technique to get partial squares


def getAllPartialSquares(n):
    result = []
    possibleRows = getAllPartialRows(n)
    print(len(possibleRows))

    def backtrack(current_square, i):
        if len(current_square) == n:
            result.append(current_square[:])
            return
        if i >= n:
            return
        for num in possibleRows:
            current_square.append(num)
            backtrack(current_square, i + 1)
            current_square.pop()
            backtrack(current_square, i + 1)
    backtrack([], 0)
    return result


def generateAllNAlgebraSizeThreePartials():
    # -----------------------------------------------------------------------------------
    # SIZE 3
    # -----------------------------------------------------------------------------------
    listOfTribracketCubesSizeThree = generateValidTribracketLatinCubes(3)
    listOfLatinSquaresSizeThree = getAllPartialSquares(3)

    generatedNAlgebras = []
    for tribracket in listOfTribracketCubesSizeThree:
        for square in listOfLatinSquaresSizeThree:
            if(isNAlgebraTest(tribracket, square)):
                generatedNAlgebras.append([tribracket, square])

    return generatedNAlgebras


def getTribracketsSizeFour():
    file = open("LatinCubes/latinCubesSize4", "rb")
    cubesSize4 = np.load(file, allow_pickle=True)
    listOfLatinCubesSizeFour = cubesSize4.tolist()
    tribrackets = []
    for cube in listOfLatinCubesSizeFour:
        if isValidTribracket(cube):
            tribrackets.append(cube)
    return tribrackets


def generateNAlgebrasSizeFourPartials():
    # -----------------------------------------------------------------------------------
    # SIZE 4
    # -----------------------------------------------------------------------------------
    listOfTribracketCubesSizeFour = getTribracketsSizeFour()
    file = open("Partials/partialSquaresSize4", "rb")
    partialSquaresSize4 = np.load(file, allow_pickle=True)
    listOfLatinSquaresSizeFour = partialSquaresSize4.tolist()

    generatedNAlgebras = []
    for tribracket in listOfTribracketCubesSizeFour:
        for square in listOfLatinSquaresSizeFour:
            if(isNAlgebraTest(tribracket, square)):
                generatedNAlgebras.append([tribracket, square])

    return generatedNAlgebras


def generateVirtualNAlgebraPartialsSizeFourGivenNAlgebras():
    file = open("Tribrackets/NAlgebrasSizeFour", "rb")
    arrayOfNAlgebrasSizeFour = np.load(file, allow_pickle=True)
    arrayOfNAlgebrasSizeFour = arrayOfNAlgebrasSizeFour.tolist()

    validNAlgebraSquares = []
    validNAlgebraCubes = []
    for NAlgebraPair in arrayOfNAlgebrasSizeFour:
        cube, square = NAlgebraPair
        if square not in validNAlgebraSquares:
            validNAlgebraSquares.append(square)
        if cube not in validNAlgebraCubes:
            validNAlgebraCubes.append(cube)

    listOfTribracketCubesSizeFour = getTribracketsSizeFour()
    generatedVirtualNAlgebras = []
    for NAlgebraTribracket in validNAlgebraCubes:
        for secondTribracket in listOfTribracketCubesSizeFour:
            for square in validNAlgebraSquares:
                if(isVirtualNAlgebraPartial(secondTribracket, square) and isNAlgebraTest(NAlgebraTribracket, square) and isVirtualTribracketTest(NAlgebraTribracket, secondTribracket)):
                    generatedVirtualNAlgebras.append(
                        [NAlgebraTribracket, secondTribracket, square])
    return generatedVirtualNAlgebras


def getInstancesExcludingFullyUndefined(NAlgebraArray):
    undefinedInstances = [
        [[1000, 1000, 1000], [1000, 1000, 1000], [1000, 1000, 1000]],
        [[1000, 1000, 1000, 1000], [1000, 1000, 1000, 1000], [
            1000, 1000, 1000, 1000], [1000, 1000, 1000, 1000]],
        ((1000, 1000, 1000), (1000, 1000, 1000), (1000, 1000, 1000)),
        ((1000, 1000, 1000, 1000), (1000, 1000, 1000, 1000),
         (1000, 1000, 1000, 1000), (1000, 1000, 1000, 1000))
    ]
    partiallyDefinedArray = []
    for pair in NAlgebraArray:
        if pair[-1] not in undefinedInstances:
            partiallyDefinedArray.append(pair)
    return partiallyDefinedArray


if __name__ == "__main__":
    print("Use functions here")

"""

Example:

[[1, 2, 3, 4], [2, 1, 4, 3], [4, 3, 1, 2], [3, 4, 2, 1]], 
[[2, 1, 4, 3], [1, 2, 3, 4], [3, 4, 2, 1], [4, 3, 1, 2]], 
[[3, 4, 2, 1], [4, 3, 1, 2], [1, 2, 3, 4], [2, 1, 4, 3]], 
[[4, 3, 1, 2], [3, 4, 2, 1], [2, 1, 4, 3], [1, 2, 3, 4]]


[[1, 2, 3, 4], [2, 1, 4, 3], [4, 3, 1, 2], [3, 4, 2, 1]]
[[2, 1, 4, 3], [1, 2, 3, 4], [3, 4, 2, 1], [4, 3, 1, 2]], 
[[3, 4, 2, 1], [4, 3, 1, 2], [1, 2, 3, 4], [2, 1, 4, 3]], 
[[4, 3, 1, 2], [3, 4, 2, 1], [2, 1, 4, 3], [1, 2, 3, 4]]

[_, 4, _, _], 
[3, _, _, _], 
[_, _, _, 1], 
[_, _, 2, _]]

"""
