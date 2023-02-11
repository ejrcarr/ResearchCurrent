import time
from latin_squares import oldGenerateArrayOfLatinSquares
from latin_squares import generateArrayOfLatinSquares
from TimeTests.tst import generateArrayOfLatinSquaresComputingRow

withoutComputingLastRow = oldGenerateArrayOfLatinSquares
computingLastRow = generateArrayOfLatinSquares
computingLastElement = generateArrayOfLatinSquaresComputingRow


def testTimeOfDifferentMethods():
    startTime = time.time()

    len(computingLastRow(1))
    len(computingLastRow(2))
    len(computingLastRow(3))
    len(computingLastRow(4))

    executionTime = (time.time() - startTime)
    print("--------------------------")
    print("COMPUTING THE LAST ROW")
    print('Execution time in seconds by computing the last row in a square: ' + str(executionTime))

    #--------------------------------------------

    startTime = time.time()

    len(withoutComputingLastRow(1))
    len(withoutComputingLastRow(2))
    len(withoutComputingLastRow(3))
    len(withoutComputingLastRow(4))

    oldExecutionTime = (time.time() - startTime)
    print()
    print('WITHOUT COMPUTING LAST ROW')
    print('Execution time in seconds: ' + str(oldExecutionTime))
    print("--------------------------")
    print("The new generation is {0:.1f} times faster than the old generation technique.".format(oldExecutionTime/executionTime))
    print("--------------------------")

testTimeOfDifferentMethods()
