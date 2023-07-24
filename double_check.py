import numpy as np
from tribracket import isValidTribracket
from virtual_tribracket import isVirtualTribracketTest

"""

This file is to double check our computations by redoing logic
without referring to the original file (partial_squares.py).

Here we also tried new implementations of the logic for the newest
axioms to confirm functionality. 

"""


def isValidPartialNAlgebra(cube, square):
    cube = np.array(cube)
    cube = (cube - 1).tolist()
    square = np.array(square)
    square = (square - 1).tolist()

    """

    1. [a, ab, b] == ab
    2. a[a, b, c] == [a, b, bc]
    3. [a, b, c] == [[a, b, bc], bc, c]
    4. [a, b, c]c == [ab, b, c]
    5. [a, b, c] == [a, ab, [ab, b, c]]

    1. [a, ab, b] == ab
    2. a[a, b, c] == [a, b, bc]
    3. [a, b, c] == [[a, b, bc], bc, c]
    4. [a, b, c]c == [ab, b, c]
    5. [a, b, c] == [a, ab, [ab, b, c]]

    """

    # Checking if positions in square are defined
    layer_length = len(cube)

    for a in range(layer_length):
        for b in range(layer_length):
            for c in range(layer_length):
                ab = square[a][b]
                bc = square[b][c]
                ABC = cube[a][b][c]
                BCA = cube[b][c][a]
                if ab < 500:      # if ab is defined (not 1000) then test
                    FAILS_FIRST_NALGEBRA_AXIOM = cube[a][ab][b] != ab
                    FAILS_FIFTH_NALEBGRA_AXIOM = ABC != cube[a][ab][cube[ab][b][c]]
                else:             # if not defined, then ignore axiom
                    FAILS_FIRST_NALGEBRA_AXIOM = False
                    FAILS_FIFTH_NALEBGRA_AXIOM = False

                if ab < 500 and square[ABC][c] < 500:
                    FAILS_FOURTH_NALGEBRA_AXIOM = square[ABC][c] != cube[ab][b][c]
                else:
                    FAILS_FOURTH_NALGEBRA_AXIOM = False

                # [a, b, c] == [[a, b, bc], bc, c]
                if bc < 500:
                    FAILS_THIRD_NALGEBRA_AXIOM = ABC != cube[cube[a]
                                                             [b][bc]][bc][c]
                else:
                    FAILS_THIRD_NALGEBRA_AXIOM = False

                # a[a, b, c] == [a, b, bc]
                if bc < 500 and square[a][ABC] < 500:
                    FAILS_SECOND_NALGEBRA_AXIOM = square[a][ABC] != cube[a][b][bc]
                else:
                    FAILS_SECOND_NALGEBRA_AXIOM = False

                if (bc > 500):
                    if (square[a][cube[a][b][c]] > 500):
                        if (square[cube[b][c][a]][a] > 500):
                            hi = "yes"
                        else:
                            return False
                    else:
                        return False
                else:
                    if (square[a][cube[a][b][c]] < 500):
                        if (square[cube[b][c][a]][a] < 500):
                            hi = "yes"
                        else:
                            return False
                    else:
                        return False

                if FAILS_FIRST_NALGEBRA_AXIOM or FAILS_SECOND_NALGEBRA_AXIOM or FAILS_THIRD_NALGEBRA_AXIOM or FAILS_FOURTH_NALGEBRA_AXIOM or FAILS_FIFTH_NALEBGRA_AXIOM:
                    return False
    return True


def isValidVirtualNAlgebraPartial(cube, square):

    cube = np.array(cube)
    cube = (cube - 1).tolist()
    square = np.array(square)
    square = (square - 1).tolist()

    """

    1. a{a, b, c} == {a, b, bc}
    2. {{a, b, bc}, bc, c} == {a, b, c}
    3. {a, b, c}c == {ab, b, c}
    4. {a, ab, {ab, b, c}} == {a, b, c}

    1. a{a, b, c} == {a, b, bc}
    2. {{a, b, bc}, bc, c} == {a, b, c}
    3. {a, b, c}c == {ab, b, c}
    4. {a, ab, {ab, b, c}} == {a, b, c}

    """
    layer_length = len(cube)

    for a in range(layer_length):
        for b in range(layer_length):
            for c in range(layer_length):

                ab = square[a][b]
                bc = square[b][c]
                ABC = cube[a][b][c]
                if (square[a][ABC] < 500) and (bc < 500):
                    FAILS_FIRST_VIRTUAL_NALGEBRA_AXIOM = square[a][ABC] != cube[a][b][bc]
                else:
                    FAILS_FIRST_VIRTUAL_NALGEBRA_AXIOM = False
                if (bc < 500):
                    FAILS_SECOND_VIRTUAL_NALGEBRA_AXIOM = cube[cube[a]
                                                               [b][bc]][bc][c] != ABC
                else:
                    FAILS_SECOND_VIRTUAL_NALGEBRA_AXIOM = False
                if (square[ABC][c] < 500) and (ab < 500):
                    FAILS_THIRD_VIRTUAL_NALGEBRA_AXIOM = square[ABC][c] != cube[ab][b][c]
                else:
                    FAILS_THIRD_VIRTUAL_NALGEBRA_AXIOM = False
                if (ab < 500):
                    FAILS_FOURTH_VIRTUAL_NALGEBRA_AXIOM = cube[a][ab][cube[ab][b][c]] != ABC
                else:
                    FAILS_FOURTH_VIRTUAL_NALGEBRA_AXIOM = False

                if FAILS_FIRST_VIRTUAL_NALGEBRA_AXIOM or FAILS_SECOND_VIRTUAL_NALGEBRA_AXIOM or FAILS_THIRD_VIRTUAL_NALGEBRA_AXIOM or FAILS_FOURTH_VIRTUAL_NALGEBRA_AXIOM:
                    return False

    return True


def getTribracketsSizeFour():
    file = open("LatinCubes/latinCubesSize4", "rb")
    cubesSize4 = np.load(file, allow_pickle=True)
    listOfLatinCubesSizeFour = cubesSize4.tolist()
    tribrackets = []
    for cube in listOfLatinCubesSizeFour:
        if isValidTribracket(cube):
            tribrackets.append(cube)
    return tribrackets


def testGenerateVirtualNAlgebraPartialsSizeFourGivenNAlgebras():
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
                if(isValidVirtualNAlgebraPartial(secondTribracket, square) and isValidPartialNAlgebra(NAlgebraTribracket, square) and isVirtualTribracketTest(NAlgebraTribracket, secondTribracket)):
                    generatedVirtualNAlgebras.append(
                        [NAlgebraTribracket, secondTribracket, square])
    return generatedVirtualNAlgebras


if __name__ == "__main__":
    print("Use functions here")
