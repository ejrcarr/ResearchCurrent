import numpy as np
from latin_cubes import generateArrayOfLatinCubes
from latin_squares import generateArrayOfLatinSquares
from tribracket import generateValidTribracketLatinCubes, isValidTribracket


'''

This class, isVirtualTribracketTest(cube, secondCube) takes in two parameters: one cube and another cube.
These cubes looks like this:    [1 2 3]   [2 3 1]   [3 1 2]
                                [3 1 2]   [1 2 3]   [2 3 1]
                                [2 3 1]   [3 1 2]   [1 2 3]

This class returns either True or False. True if both cubes are compatable to be a Virtual Tribracket.

'''


def isVirtualTribracketTest(cube, secondCube):
    '''
    These first fourlines in the code - 40, 41, 44, 45
    Makes each element of cube one less so that it is indexable since having a value equal length would be an error: index out of bounds.
    Index begins at 0 so if I were to access the third element in the array, [5, 6, 7]    I would code: array[2] and if I accidently typed array[3] I would-
                                                                              ^  ^  ^  ^               -get an error since the max index is 2 in this array.
                                                                              0  1  2  3
    eg.

        [1 2 3]   [2 3 1]   [3 1 2]
        [3 1 2]   [1 2 3]   [2 3 1]
        [2 3 1]   [3 1 2]   [1 2 3]

                    |
                    v

        [0 1 2]   [1 2 0]   [2 0 1]
        [2 0 1]   [0 1 2]   [1 2 0]
        [1 2 0]   [2 0 1]   [0 1 2]

    '''

    # Converting this cube into a numpy cube makes it more readable to subtract one from each element.
    cube = np.array(cube)
    # After subtracting one from each element in the array (cube - 1), I convert it into a python list to handle.
    cube = (cube - 1).tolist()

    # This cube too
    secondCube = np.array(secondCube)
    secondCube = (secondCube - 1).tolist()

    '''

    Now that both cubes are indexable with values 0 - 2, we now go through all possible combinations of a, b, c, and d
    So  e.g   a b c d    since len(rowLength) = 3     -------------
              0 0 0 0                                 |  [0 1 2]  |   [1 2 0]   [2 0 1]                   [0 1 2] <----
              0 0 0 1                      cube[0] =  |  [2 0 1]  |   [0 1 2]   [1 2 0]     cube[0][0] =  [2 0 1]        len(cube[0][0]) = 3 since [0 1 2]
              0 0 0 2                                 |  [1 2 0]  |   [2 0 1]   [0 1 2]                   [1 2 0]                            has three elements
                                                      -------------
    '''
    rowLength = len(cube[0][0])                     # Explanation ^

    for a in range(rowLength):  # range(rowLength) will loop through 0, 1, 2
        for b in range(rowLength):
            for c in range(rowLength):
                for d in range(rowLength):

                    '''

                    { } = angle brackets
                    [ ] = square brackets

                    1. [a, b, [b, c, d]] = [a, [a, b, c], [[a, b, c], c, d]]
                    2. [[a, b, c], c, d] = [[a, b, [b, c, d]], [b, c, d], d]  Mistake in paper right side of equals first element has too many ending brackets
                    3. {a, {a, b, c}, c} = b
                    4. {a, b, {b, c, d}} = {a, {a, b, c}, {{a, b, c}, c, d}}
                    5. {{a, b, c}, c, d} = {{a, b, {b, c, d}}, {b, c, d}, d}
                    6. [{a, b, c}, c, d] = {[a, b, {b, c, d}], {b, c, d}, d}
                    7. [a, b, {b, c, d}] = {a, {a, b, c}, [{a, b, c}, c, d]}

                    '''

                    FAILS_FIRST_EQUATION = cube[a][b][cube[b][c][d]
                                                      ] != cube[a][cube[a][b][c]][cube[cube[a][b][c]][c][d]]
                    FAILS_SECOND_EQUATION = cube[cube[a][b][c]
                                                 ][c][d] != cube[cube[a][b][cube[b][c][d]]][cube[b][c][d]][d]
                    FAILS_THIRD_EQUATION = secondCube[a][secondCube[a]
                                                         [b][c]][c] != b
                    FAILS_FOURTH_EQUATION = secondCube[a][b][secondCube[b][c][d]
                                                             ] != secondCube[a][secondCube[a][b][c]][secondCube[secondCube[a][b][c]][c][d]]
                    FAILS_FIFTH_EQUATION = secondCube[secondCube[a][b][c]
                                                      ][c][d] != secondCube[secondCube[a][b][secondCube[b][c][d]]][secondCube[b][c][d]][d]
                    FAILS_SIXTH_EQUATION = cube[secondCube[a][b][c]][c][d] != secondCube[cube[a]
                                                                                         [b][secondCube[b][c][d]]][secondCube[b][c][d]][d]
                    FAILS_SEVENTH_EQUATION = cube[a][b][secondCube[b][c][d]
                                                        ] != secondCube[a][secondCube[a][b][c]][cube[secondCube[a][b][c]][c][d]]

                    # If any of these conditions are true, then the function returns False --> that these cubes are NOT compatable.
                    if FAILS_FIRST_EQUATION or FAILS_SECOND_EQUATION or FAILS_THIRD_EQUATION or FAILS_FOURTH_EQUATION or FAILS_FIFTH_EQUATION or FAILS_SIXTH_EQUATION or FAILS_SEVENTH_EQUATION:
                        # If this statement is executed, then the whole function will stop since it has returned a value -- EVEN IF the for loops are not done.
                        # Therefore, if any of these functions are True and these cubes FAIL a test then the function ends early and returns False
                        return False

    # If the function has gone through every possible combination of a b c d from  0 0 0 0  to  2 2 2 2 and the function
    # is still executing/hasn't returned false then that means it has passed all cases and the cubes are therefore compatable.
    return True


'''

This class, isNAlgebraTest(cube, square), takes in two parameters: the first cube and a square.
The cube looks like this:       [1 2 3]   [2 3 1]   [3 1 2]     and square like this:     [1 2 3]
                                [3 1 2]   [1 2 3]   [2 3 1]                               [3 1 2]
                                [2 3 1]   [3 1 2]   [1 2 3]                               [2 3 1]

This class returns either True or False. True if the cube and square are compatable to be an Niebrzydowski Algebra.

'''
falseArray = [0, 0, 0, 0, 0]
sumArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
freq = [0, 0, 0, 0, 0]


def isNAlgebraTest(cube, square):

    # These four lines make the cube and the square indexable by subtracting one from each element. See above (lines 19-38) if need visualization.
    cube = np.array(cube)
    cube = (cube - 1).tolist()
    square = np.array(square)
    square = (square - 1).tolist()

    rowLength = len(cube[0][0])

    # Since testing if a cube and a square are Valid N-Algebras only require  a, b, c then there are only 3 for-loops.
    for a in range(rowLength):
        for b in range(rowLength):
            for c in range(rowLength):

                '''

                1. [a, ab, b] = ab
                2. a[a, b, c] = [a, b, bc]
                3. [a, b, c] = [[a, b, bc], bc, c]
                4. [a, b, c]c = [ab, b, c]
                5. [a, b, c] = [a, ab, [ab, b, c]]

                '''

                # These conditions do not check if the cube is a tribracket since I am already checking in the above function.
                FAILS_FIRST_SQUARE_BRACKET = cube[a][square[a]
                                                     [b]][b] != square[a][b]
                FAILS_SECOND_SQUARE_BRACKET = square[a][cube[a]
                                                        [b][c]] != cube[a][b][square[b][c]]
                FAILS_THIRD_SQUARE_BRACKET = cube[a][b][c] != cube[cube[a]
                                                                   [b][square[b][c]]][square[b][c]][c]
                FAILS_FOURTH_SQUARE_BRACKET = square[cube[a]
                                                     [b][c]][c] != cube[square[a][b]][b][c]
                FAILS_FIFTH_SQUARE_BRACKET = cube[a][b][c] != cube[a][square[a]
                                                                      [b]][cube[square[a][b]][b][c]]

                # If fails any of the above axioms then function ends early and returns False
                if FAILS_FIRST_SQUARE_BRACKET or FAILS_SECOND_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET:
                    if (FAILS_FIRST_SQUARE_BRACKET and not (FAILS_SECOND_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET)):
                        falseArray[0] += 1
                    if (FAILS_SECOND_SQUARE_BRACKET and not (FAILS_FIRST_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET)):
                        falseArray[1] += 1
                    if (FAILS_THIRD_SQUARE_BRACKET and not (FAILS_SECOND_SQUARE_BRACKET or FAILS_FIRST_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET)):
                        falseArray[2] += 1
                    if (FAILS_FOURTH_SQUARE_BRACKET and not (FAILS_SECOND_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FIRST_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET)):
                        falseArray[3] += 1
                    if (FAILS_FIFTH_SQUARE_BRACKET and not (FAILS_SECOND_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIRST_SQUARE_BRACKET)):
                        falseArray[4] += 1

                    # if FAILS_THIRD_SQUARE_BRACKET:
                    #     # if (FAILS_FIRST_SQUARE_BRACKET and not (FAILS_SECOND_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET)):
                    #     #     falseArray[0] += 1
                    #     # if (FAILS_SECOND_SQUARE_BRACKET and not (FAILS_FIRST_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET)):
                    #     #     falseArray[1] += 1
                    #     # if (FAILS_THIRD_SQUARE_BRACKET and not (FAILS_SECOND_SQUARE_BRACKET or FAILS_FIRST_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET)):
                    #     #     falseArray[2] += 1
                    #     # if (FAILS_FOURTH_SQUARE_BRACKET and not (FAILS_SECOND_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FIRST_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET)):
                    #     #     falseArray[3] += 1
                    #     # if (FAILS_FIFTH_SQUARE_BRACKET and not (FAILS_SECOND_SQUARE_BRACKET or FAILS_THIRD_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIRST_SQUARE_BRACKET)):
                    #     #     falseArray[4] += 1
                    #     if FAILS_FIRST_SQUARE_BRACKET:
                    #         falseArray[0] += 1
                    #     if FAILS_SECOND_SQUARE_BRACKET:
                    #         falseArray[1] += 1
                    #     if FAILS_THIRD_SQUARE_BRACKET:
                    #         falseArray[2] += 1
                    #     if FAILS_FOURTH_SQUARE_BRACKET:
                    #         falseArray[3] += 1
                    #     if FAILS_FIFTH_SQUARE_BRACKET:
                    #         falseArray[4] += 1

                    # print("1.", FAILS_FIRST_SQUARE_BRACKET)
                    # print("2.", FAILS_SECOND_SQUARE_BRACKET)
                    # print("3.", FAILS_THIRD_SQUARE_BRACKET)
                    # print("4.", FAILS_FOURTH_SQUARE_BRACKET)
                    # print("5.", FAILS_FIFTH_SQUARE_BRACKET)
                    return False

                # if FAILS_FIRST_SQUARE_BRACKET or FAILS_SECOND_SQUARE_BRACKET or FAILS_FOURTH_SQUARE_BRACKET or FAILS_FIFTH_SQUARE_BRACKET:
                #     return False

    # If for-loops end then that means they are compatable.
    return True


'''

This class, isVirtualNAlgebraTest(secondCube, square), takes in two parameters: the second cube and a square.
The cube looks like this:       [1 2 3]   [2 3 1]   [3 1 2]     and square like this:     [1 2 3]
                                [3 1 2]   [1 2 3]   [2 3 1]                               [3 1 2]
                                [2 3 1]   [3 1 2]   [1 2 3]                               [2 3 1]

This class returns either True or False. True if the second cube and square are compatable to be an Virtual Niebrzydowski Algebra.

'''


def isVirtualNAlgebraTest(secondCube, square):

    # These four lines make the cube and the square indexable by subtracting one from each element. See above (lines 19-38) if need visualization.
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
                FAILS_FIRST_ANGLE_BRACKET = square[a][secondCube[a]
                                                      [b][c]] != secondCube[a][b][square[b][c]]
                FAILS_SECOND_ANGLE_BRACKET = secondCube[a][b][c] != secondCube[secondCube[a]
                                                                               [b][square[b][c]]][square[b][c]][c]
                FAILS_THIRD_ANGLE_BRACKET = square[secondCube[a]
                                                   [b][c]][c] != secondCube[square[a][b]][b][c]
                FAILS_FOURTH_ANGLE_BRACKET = secondCube[a][square[a][b]
                                                           ][secondCube[square[a][b]][b][c]] != secondCube[a][b][c]

                if FAILS_FIRST_ANGLE_BRACKET or FAILS_SECOND_ANGLE_BRACKET or FAILS_THIRD_ANGLE_BRACKET or FAILS_FOURTH_ANGLE_BRACKET:
                    return False

    return True


'''

This function takes in two cubes and a square and returns if this combination is a viable virtual N algebra Tribracket.

'''


def isValidVirtualNAlgebraTribracket(cube, secondCube, square):
    # If these cubes are incompatable to be Virtual Tribrackets or are not valid Tribrackets then we return False.
    if not isVirtualTribracketTest(cube, secondCube):
        return False
    # If the first cube and the square are incompatable to be a Niebrzydowski Algebra then it returns False
    if not isNAlgebraTest(cube, square):
        return False
    # If the second cube and the square are incompatable to be a Virtual Niebrzydowski Algebra then it returns False
    if not isVirtualNAlgebraTest(secondCube, square):
        return False

    # If passes all of theses tests, then this combination is a valid virtual Niebrzydowski algebras.
    return True


'''

This function generates valid Tribrackets size n from latin squares.

'''


def generateValidTribracketLatinCubes(sizeOfCube):
    # Edge cases
    if sizeOfCube == 0:
        return []
    elif sizeOfCube == 1:
        return [0]

    # Total Row Sum is the number of all added elements in a single row.
    #   e.g.  [1, 2, 3, 4] = 10 because 1 + 2 + 3 + 4 = 10.
    #       This is eventually used to calculate the last element of a cube.
    #   e.g.  [1, 2, 3, ?] --> (10 - 1 - 2 - 3) = 4
    TOTAL_ROW_SUM = sum([i for i in range(1, sizeOfCube+1)])

    # We generate an array of valid squares to generate cubes without having to create cubes by
    # creating each individual element. Instead, we use already calculated Latin Squares.
    # We also don't have to worry about rows or columns having duplicate elements. We just have to worry
    # about the z-axis.
    validSquares = generateArrayOfLatinSquares(sizeOfCube)

    # Initialize empty array for the new generated cubes
    generatedLatinCubes = []

    # Creates a same length cube with all 0s to reset currentLatinCube
    #   [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]
    #   [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]
    #   [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]
    #   [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]

    defaultCube = [[[0 for i in range(sizeOfCube)] for i in range(
        sizeOfCube)] for i in range(sizeOfCube)]
    currentLatinCube = defaultCube[:]

    n = sizeOfCube - 1
    # Creates an array that will essentially be adding nested for-loops
    # dependent on the size of the array. If size = 4 then n = 4-1
    # dynamicArray = [0, 0, 0, 0] since i executes n + 1 (4) times.
    dynamicArray = [0 for i in range(n+1)]

    # Max is the length of array of valid Squares
    # It is going to loop through each combination of squares from [0, 0, 0, 0] to [576, 576, 576, 0] if size = 4.
    # Once the last element changes, then the while loop exists since the condition(dynamicArray[n] == 0) is not met.
    #       Note: n = 3 since size = 4 --> n = 4 - 1
    MAX = len(validSquares)
    p = 0

    # Execute the code underneath while the last element is 0. [576, 576, 576, 0] because then we would have seen each combination.
    #                                                                          ^
    while dynamicArray[n] == 0:
        # Trick to only go through this code if there are all squares are unique.
        # [576, 576, 576] would not execute because there are no repeats in a list
        # so the set would be (576) which is length = 1. However, [1, 2, 3] would
        # execute because there are no repeats so the set would be (1, 2, 3) which
        # is the same length.
        #   Note: the [:n] at the end of the array is called SPLICING which cuts off the array at index n not inclusive.
        #         so [576, 576, 576, 0] becomes [576, 576, 576]  https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
        if(len(dynamicArray[:n]) == len(set(dynamicArray[:n]))):

            # This for loop fills in the first n-1 squares in the cube so that we can compute the last.
            #   [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]
            #   [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]
            #   [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]
            #   [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]
            #                                 |
            #                                 v
            #   [1, 2, 3, 4]    [2, 3, 4, 1]    [3, 4, 1, 2]    [0, 0, 0, 0]
            #   [2, 3, 4, 1]    [3, 4, 1, 2]    [4, 1, 2, 3]    [0, 0, 0, 0]
            #   [3, 4, 1, 2]    [4, 1, 2, 3]    [1, 2, 3, 4]    [0, 0, 0, 0]
            #   [4, 1, 2, 3]    [1, 2, 3, 4]    [2, 3, 4, 1]    [0, 0, 0, 0]
            for i in range(sizeOfCube-1):
                currentLatinCube[i] = validSquares[dynamicArray[i]]

            # Computes the last square from given three squares
            newSquare = []
            newRow = []
            sumOfCurrentColumns = 0
            for columnIndex in range(sizeOfCube):
                for rowIndex in range(sizeOfCube):
                    for cubeIndex in range(sizeOfCube-1):
                        sumOfCurrentColumns += currentLatinCube[cubeIndex][columnIndex][rowIndex]
                    # Gather an array of new values e.g. [2, 3, 1, 4]
                    newRow.append(TOTAL_ROW_SUM - sumOfCurrentColumns)
                    sumOfCurrentColumns = 0  # Reset current sum
                # When the row is finished, add it to the current square
                newSquare.append(newRow[:])
                newRow = []                 # and reset the new row.

            # Make our new, computed square the last square in the cube
            currentLatinCube[sizeOfCube - 1] = newSquare[:]

            # Then test it and add it to the array if it is valid
            if(isValidTribracket(currentLatinCube)):
                generatedLatinCubes.append(currentLatinCube)

            # Reset cube to all 0s when done.
            currentLatinCube = defaultCube[:]

        # e.g.   [(20 + 1), 25, 27, 0]
        dynamicArray[0] += 1

        # Resets other indexes to 0 if it reaches max so
        # e.g.   [576, 576, 5, 0] --> [0, 0, 6, 0]
        while dynamicArray[p] == MAX:
            dynamicArray[p] = 0
            p += 1
            dynamicArray[p] += 1
            if dynamicArray[p] != MAX:
                p = 0

    return generatedLatinCubes


'''

generateVirtualNAlgebrasSizeThree() generates an array of Valid Tribracket Latin Cubes size 3 as well as an array of Latin Squares size 3
and generates every combination of cube, cube, square and calls the function isValidVirtualNAlgebraTribracket(tribracket, secondTribracket, square)
to check if these are a valid NAlgebraTribracket. If they are, the cube, second cube, and square are added to an array of current working pairs.

Returns an array of Virtual N-Algebras Size 3

'''


def generateVirtualNAlgebrasSizeThree():
    # -----------------------------------------------------------------------------------
    # SIZE 3
    # -----------------------------------------------------------------------------------
    #  listOfTribracketCubesSizeThree = generateValidTribracketLatinCubes(3)
    #  listOfLatinSquaresSizeThree = generateArrayOfLatinSquares(3)

    #  generatedNAlgebras = []
    #  for tribracket in listOfTribracketCubesSizeThree:
    #     for secondTribracket in listOfTribracketCubesSizeThree:
    #         for square in listOfLatinSquaresSizeThree:
    #             if(isValidVirtualNAlgebraTribracket(tribracket, secondTribracket, square)):
    #                 generatedNAlgebras.append([tribracket, secondTribracket, square])

    # -----------------------------------------------------------------------------------
    # SIZE 4
    # -----------------------------------------------------------------------------------
    file = open("Tribrackets/tribracketCubesSizeFour", "rb")
    arrayOfTribracketsSize4 = np.load(file, allow_pickle=True)
    arrayOfTribracketsSize4 = arrayOfTribracketsSize4.tolist()

    listOfLatinSquaresSizeFour = generateArrayOfLatinSquares(4)

    generatedNAlgebras = []
    for tribracket in arrayOfTribracketsSize4:
        for secondTribracket in arrayOfTribracketsSize4:
            for square in listOfLatinSquaresSizeFour:
                print(arrayOfTribracketsSize4.index(tribracket))
                if(isValidVirtualNAlgebraTribracket(tribracket, secondTribracket, square)):
                    generatedNAlgebras.append(
                        [tribracket, secondTribracket, square])

    return generatedNAlgebras


'''

generateVirtualTribracketSizeThree() only generates the valid combinations of any two given cubes.
It first generates an array of Tribracket Latin Cubes size three and goes through each combination.
If a given combination works then the pair is added to an array.

Returns an array of Virtual Tribrackets Size 3

'''


def generateVirtualTribracketSizeThree():
    # -----------------------------------------------------------------------------------
    # SIZE 3
    # -----------------------------------------------------------------------------------
    listOfTribracketCubesSizeThree = generateValidTribracketLatinCubes(3)

    generatedNAlgebras = []
    for tribracket in listOfTribracketCubesSizeThree:
        for secondTribracket in listOfTribracketCubesSizeThree:
            if(isVirtualTribracketTest(tribracket, secondTribracket)):
                generatedNAlgebras.append([tribracket, secondTribracket])

    # -----------------------------------------------------------------------------------
    # SIZE 4
    # -----------------------------------------------------------------------------------
    # file = open("Tribrackets/TribracketsSizeFour", "rb")
    # arrayOfTribracketsSize4 = np.load(file, allow_pickle=True)
    # arrayOfTribracketsSize4 = arrayOfTribracketsSize4.tolist()

    # generatedNAlgebras = []
    # for tribracket in arrayOfTribracketsSize4:
    #     for secondTribracket in arrayOfTribracketsSize4:
    #         if(isVirtualTribracketTest(tribracket, secondTribracket)):
    #             generatedNAlgebras.append([tribracket, secondTribracket])

    return generatedNAlgebras


'''

generateNAlgebraSizeThree() generates an array of Valid Tribracket Latin Cubes size 3 as well as an array of Latin Squares size 3
and generates every combination of cube and square and calls the function isNAlgebraTest(tribracket, square)
to check if these are a valid NAlgebra. If they are, the cube and square are added to an array of current working pairs.

Returns an array of N-Algebras Size 3

'''


def generateNAlgebraSizeThree():
    # -----------------------------------------------------------------------------------
    # SIZE 3
    # -----------------------------------------------------------------------------------
    listOfTribracketCubesSizeThree = generateValidTribracketLatinCubes(3)
    #  print(len(listOfTribracketCubesSizeThree))
    listOfLatinSquaresSizeThree = generateArrayOfLatinSquares(3)
    #  print(len(listOfLatinSquaresSizeThree))

    generatedNAlgebras = []
    for tribracket in listOfTribracketCubesSizeThree:
        for square in listOfLatinSquaresSizeThree:
            if(isNAlgebraTest(tribracket, square)):
                generatedNAlgebras.append([tribracket, square])

    # -----------------------------------------------------------------------------------
    # SIZE 4
    # -----------------------------------------------------------------------------------
    #  file = open("Tribrackets/tribracketCubesSizeFour", "rb")
    #  arrayOfTribracketsSize4 = np.load(file, allow_pickle=True)
    #  arrayOfTribracketsSize4 = arrayOfTribracketsSize4.tolist()

    #  listOfLatinSquaresSizeFour = generateArrayOfLatinSquares(4)

    #  generatedNAlgebras = []
    #  for tribracket in arrayOfTribracketsSize4:
    #     for square in listOfLatinSquaresSizeFour:
    #         print(arrayOfTribracketsSize4.index(tribracket))
    #         if(isNAlgebraTest(tribracket, square)):
    #             generatedNAlgebras.append([tribracket, square])

    return generatedNAlgebras


if __name__ == "__main__":
    # virtualNAlgebras = generateVirtualNAlgebrasSizeThree()

    # THIS ---
    # NAlgebras = generateNAlgebraSizeThree()

    print(len(generateVirtualTribracketSizeThree()))

    # virtualTribrackets = generateVirtualTribracketSizeThree()
    # print(len(virtualTribrackets))
    # tribrackets = generateValidTribracketLatinCubes(3)

    # for pair in virtualNAlgebras:
    #     for thing in pair:
    #         print(thing)
    #     print()

    # print(len(virtualNAlgebras))

    # for pair in NAlgebras:
    #     for thing in pair:
    #         print(thing)
    #     print()

    # THESE -----
    # print(len(NAlgebras))
    # print(freq)
    # print(sumArray)
    # print(falseArray)

    # -------------------------------------------------------------

    # 12 * 12 = 144
    # FREQ THREE = [  97  ,  73  ,  97  ,  84  ,  104  ]
    #              [  67% ,  50% ,  67% ,  58% ,  72%  ]

    # 168 * 576 = 96768
    # FREQ FOUR = [65742, 61532, 65700, 70084, 71780]
    #             [ 68%,   63%,   68%,   72%,   74% ]
    #                       ^             ^

    # AMOUNT OF VIRTUAL TRIBRACKETS SIZE FOUR = 1080
    # AMOUNT OF TRIBRACKETS SIZE FOUR = 168
    # AMOUNT OF N-ALGEBRAS SIZE FOUR = 0   :(
    # AMOUNT OF VIRTUAL N-ALGEBRAS SIZE FOUR = ? probably 0

    # -------------------------------------------------------------

    # for pair in virtualNAlgebras:
    #     for thing in pair:
    #         print(thing)
    #     print()

    # for pair in virtualNAlgebras:
    #     for thing in pair:
    #         print(thing)
    #     print()

    # -----------------------------------------------------------------------------------
    # Writing to files
    # -----------------------------------------------------------------------------------

    # arrayOfVirtualNAlgebrasSizeThree = np.array(tempVar, dtype=object)
    # file = open("Tribrackets/VirtualNAlgebrasSizeThree", "wb")
    # np.save(file, arrayOfVirtualNAlgebrasSizeThree)
    # file.close

    # arrayOfNAlgebrasSizeThree = np.array(tempVar, dtype=object)
    # file = open("Tribrackets/NAlgebrasSizeThree", "wb")
    # np.save(file, arrayOfNAlgebrasSizeThree)
    # file.close

    # arrayOfVirtualTribracketsSizeThree = np.array(tempVar, dtype=object)
    # file = open("Tribrackets/VirtualTribracketsSizeThree", "wb")
    # np.save(file, arrayOfVirtualTribracketsSizeThree)
    # file.close

    # arrayOfTribracketsSizeThree = np.array(tempVar, dtype=object)
    # file = open("Tribrackets/TribracketsSizeThree", "wb")
    # np.save(file, arrayOfTribracketsSizeThree)
    # file.close

    # -----------------------------------------------------------------------------------
    # Reading in files
    # -----------------------------------------------------------------------------------

    # file = open("Tribrackets/VirtualNAlgebrasSizeThree", "rb")
    # arrayOfVirtualNAlgebrasSizeThree = np.load(file, allow_pickle=True)
    # arrayOfVirtualNAlgebrasSizeThree = arrayOfVirtualNAlgebrasSizeThree.tolist()

    # file = open("Tribrackets/NAlgebrasSizeThree", "rb")
    # arrayOfNAlgebrasSizeThree = np.load(file, allow_pickle=True)
    # arrayOfNAlgebrasSizeThree = arrayOfNAlgebrasSizeThree.tolist()

    # file = open("Tribrackets/VirtualTribracketsSizeThree", "rb")
    # arrayOfVirtualTribracketsSizeThree = np.load(file, allow_pickle=True)
    # arrayOfVirtualTribracketsSizeThree = arrayOfVirtualTribracketsSizeThree.tolist()

    # file = open("Tribrackets/TribracketsSizeThree", "rb")
    # arrayOfTribracketsSizeThree = np.load(file, allow_pickle=True)
    # arrayOfTribracketsSizeThree = arrayOfTribracketsSizeThree.tolist()
    # print(len(arrayOfTribracketsSizeThree))

    # -----------------------------------------------------------------------------------

    # print(len(generateValidTribracketLatinCubes(3)))
    # print(len(generateNAlgebrasSizeThree()))

    # for pair in arrayOfVirtualTribracketsSizeThree:
    #     for thing in pair:
    #         print(thing)
    #         # print(np.array(thing))
    #     print()

    """

    Virtual Niebrzydowski Algebra (1)
    [[(1, 2, 3), (3, 1, 2), (2, 3, 1)], [(2, 3, 1), (1, 2, 3), (3, 1, 2)], [[3, 1, 2], [2, 3, 1], [1, 2, 3]]]
    [[(1, 2, 3), (3, 1, 2), (2, 3, 1)], [(2, 3, 1), (1, 2, 3), (3, 1, 2)], [[3, 1, 2], [2, 3, 1], [1, 2, 3]]]
    [(1, 3, 2), (3, 2, 1), (2, 1, 3)]

                        |
                        |  Formatted
                        v

            [1 2 3]   [2 3 1]   [3 1 2]
            [3 1 2]   [1 2 3]   [2 3 1]         Cube One
            [2 3 1]   [3 1 2]   [1 2 3]

            [1 2 3]   [2 3 1]   [3 1 2]
            [3 1 2]   [1 2 3]   [2 3 1]         Cube Two
            [2 3 1]   [3 1 2]   [1 2 3]

            [1 3 2]
            [3 2 1]     Square
            [2 1 3]

    """

    # if FAILS_FIRST_SQUARE_BRACKET:
    #     freq[0] += 1
    # if FAILS_SECOND_SQUARE_BRACKET:
    #     freq[1] += 1
    # if FAILS_THIRD_SQUARE_BRACKET:
    #     freq[2] += 1
    # if FAILS_FOURTH_SQUARE_BRACKET:
    #     freq[3] += 1
    # if FAILS_FIFTH_SQUARE_BRACKET:
    #     freq[4] += 1
    # if FAILS_THIRD_SQUARE_BRACKET and FAILS_FIRST_SQUARE_BRACKET:
    #     sum[0] += 1
    # if FAILS_FIRST_SQUARE_BRACKET and FAILS_SECOND_SQUARE_BRACKET:
    #     sum[1] += 1
    # if FAILS_FIRST_SQUARE_BRACKET and FAILS_FOURTH_SQUARE_BRACKET:
    #     sum[2] += 1
    # if FAILS_FIRST_SQUARE_BRACKET and FAILS_FIFTH_SQUARE_BRACKET:
    #     sum[3] += 1
    # if FAILS_SECOND_SQUARE_BRACKET and FAILS_THIRD_SQUARE_BRACKET:
    #     sum[4] += 1
    # if FAILS_SECOND_SQUARE_BRACKET and FAILS_FOURTH_SQUARE_BRACKET:
    #     sum[5] += 1
    # if FAILS_SECOND_SQUARE_BRACKET and FAILS_FIFTH_SQUARE_BRACKET:
    #     sum[6] += 1
    # if FAILS_THIRD_SQUARE_BRACKET and FAILS_FOURTH_SQUARE_BRACKET:
    #     sum[7] += 1
    # if FAILS_THIRD_SQUARE_BRACKET and FAILS_FIFTH_SQUARE_BRACKET:
    #     sum[8] += 1
    # if FAILS_FOURTH_SQUARE_BRACKET and FAILS_FIFTH_SQUARE_BRACKET:
    #     sum[9] += 1
