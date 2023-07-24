import numpy as np
from latin_cubes import generateArrayOfLatinCubes
from latin_squares import generateArrayOfLatinSquares

from partial_squares import generateNAlgebraOrderNPartials, generateVirtualNAlgebrasOrderNPartials, getAllPartialSquares
from tribracket import generateValidTribracketLatinCubes
from virtual_tribracket import generateNAlgebraOrderN, generateVirtualNAlgebrasOrderN

# This function will create a file in the root directory of the project
# which will display all of the information of the order N


def writeInformationOfOrderNToFile(size, filename):
    file = open(f'{filename}.txt', "w+")

    squares = generateArrayOfLatinSquares(size)
    numberOfSquares = len(squares)
    file.write(f'Number of squares order {size}: {numberOfSquares}\n')

    cubes = generateArrayOfLatinCubes(size)
    numberOfCubes = len(cubes)
    file.write(f'Number of cubes order {size}: {numberOfCubes}\n')

    partialSquares = getAllPartialSquares(size)
    numberOfPartialSquares = len(partialSquares)
    file.write(f'Number of partial squares order {size}: {numberOfPartialSquares}\n')

    tribracketCubes = generateValidTribracketLatinCubes(size)
    numberOfTribracketCubes = len(tribracketCubes)
    file.write(f'Number of tribracket cubes order {size}: {numberOfTribracketCubes}\n')

    NAlgebraPairs = generateNAlgebraOrderN(tribracketCubes, squares)
    numberOfNAlgebraPairs = len(NAlgebraPairs)
    file.write(f'Number of NAlgebra pairs order {size}: {numberOfNAlgebraPairs}\n')

    virtualNAlgebraPairs = generateVirtualNAlgebrasOrderN(tribracketCubes, squares)
    numberOfVirtualNAlgebraPairs = len(virtualNAlgebraPairs)
    file.write(f'Number of virtual NAlgebra pairs order {size}: {numberOfVirtualNAlgebraPairs}\n')

    partialNAlgebraPairs = generateNAlgebraOrderNPartials(tribracketCubes, partialSquares)
    numberOfPartialNAlgebraPairs = len(partialNAlgebraPairs)
    file.write(f'Number of partial NAlgebra pairs order {size}: {numberOfPartialNAlgebraPairs}\n')

    partialVirtualNAlgebrasPairs = generateVirtualNAlgebrasOrderNPartials(tribracketCubes, partialSquares)
    numberOfPartialVirtualNAlgebrasPairs = len(partialVirtualNAlgebrasPairs)
    file.write(f'Number of partial virtual NAlgebra pairs order {size}: {numberOfPartialVirtualNAlgebrasPairs}\n')

    file.close


if __name__ == "__main__":
    print("Write function calls here")

    # Example of how to call the function:
    # writeInformationOfOrderNToFile(3, "OrderThree")
