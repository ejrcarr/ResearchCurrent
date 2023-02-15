import numpy as np
from latin_squares import generateArrayOfLatinSquares
from tribracket import generateValidTribracketLatinCubes
from virtual_tribracket import isValidVirtualNAlgebraTribracket, isVirtualTribracketTest


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
        print(i)
        for square in testArray[i].copy():
            print('here ', i)
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

    # print(len(testArray[-1]))

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

                # print("First", FAILS_FIRST_SQUARE_BRACKET)
                # print("Second", FAILS_SECOND_SQUARE_BRACKET)
                # print("Third", FAILS_THIRD_SQUARE_BRACKET)
                # print("Fourth: ", FAILS_FOURTH_SQUARE_BRACKET, (square[abc][c] if square[abc][c] > 0 else abCbCc), "!=", (abCbCc if abCbCc > 0 else square[abc][c]))
                # print("Fifth", FAILS_FIFTH_SQUARE_BRACKET)
                # FAILS_FIRST_SQUARE_BRACKET = aabb != ab
                # FAILS_SECOND_SQUARE_BRACKET = aabc != aCbCbc
                # FAILS_THIRD_SQUARE_BRACKET = abc != cube[aCbCbc][bc][c]
                # FAILS_FOURTH_SQUARE_BRACKET = square[abc][c] != abCbCc
                # FAILS_FIFTH_SQUARE_BRACKET = abc != cube[a][ab][abCbCc]

                # a[a, b, c] <-> bc

                # For all b and c, bc is defined if and only if a[a, b, c] and [b, c, a]a are defined for all a
                # if(a == 0 and b == 2 and c == 0):
                #     print(square[b][c], "!=", square[a][cube[a][b][c]])

                if(square[b][c] > 500 and (square[a][cube[a][b][c]] < 500 or square[cube[b][c][a]][a] < 500)):
                    return False
                if(square[b][c] < 500 and (square[a][cube[a][b][c]] > 500 or square[cube[b][c][a]][a] > 500)):
                    return False

                # if(square[b][c] != square[a][cube[a][b][c]] != square[cube[b][c][a]][a]):
                #     return False

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
                # FAILS_FIRST_ANGLE_BRACKET = square[a][secondCube[a][b][c]] != secondCube[a][b][square[b][c]]
                # FAILS_SECOND_ANGLE_BRACKET = secondCube[a][b][c] != secondCube[secondCube[a][b][square[b][c]]][square[b][c]][c]
                # FAILS_THIRD_ANGLE_BRACKET = square[secondCube[a][b][c]][c] != secondCube[square[a][b]][b][c]
                # FAILS_FOURTH_ANGLE_BRACKET = secondCube[a][square[a][b]][secondCube[square[a][b]][b][c]] != secondCube[a][b][c]

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
                    # if(isValidVirtualNAlgebraTribracket(tribracket, secondTribracket, square)):
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


def generateNAlgebraSizeFourPartials():
    # -----------------------------------------------------------------------------------
    # SIZE 4
    # -----------------------------------------------------------------------------------
    listOfTribracketCubesSizeFour = generateValidTribracketLatinCubes(4)
    file = open("Partials/partialSquaresSize4", "rb")
    listOfLatinSquaresSizeFour = np.load(file, allow_pickle=True)
    listOfLatinSquaresSizeFour = listOfLatinSquaresSizeFour.tolist()

    generatedNAlgebras = []
    for tribracket in listOfTribracketCubesSizeFour:
        for square in listOfLatinSquaresSizeFour:
            if(isNAlgebraTest(tribracket, square)):
                generatedNAlgebras.append([tribracket, square])

    return generatedNAlgebras


if __name__ == "__main__":
    arrayOfPartialSquaresSizeFour = generateArrayOfPartialSquares(4)
    partialsSizeFour = np.array(arrayOfPartialSquaresSizeFour, dtype=object)
    file = open("Partials/partialSquaresSize4", "wb")
    np.save(file, partialsSizeFour)
    file.close

    arrayOfNAlgebraSizeFourPartial = generateNAlgebraSizeFourPartials()
    partialsNAlgebrasSizeFour = np.array(
        arrayOfNAlgebraSizeFourPartial, dtype=object)
    file = open("Partials/partialNAlgebrasSize4", "wb")
    np.save(file, partialsNAlgebrasSizeFour)
    file.close
