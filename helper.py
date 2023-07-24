import numpy as np

"""

This file is to provide functions to save results of function calls.


Usage Guides:

writeArrayToFile(variable, filename)
    - To call function, import the function from the file named "helper"
        - "from helper import writeArrayToFile"
    - Then for the first parameter, variable, you store whatever variable
      that is holding the array of a function call.
    - For the second parameter, you put any string that you want to name 
      the file. This will be the name in which you retrieve the array using
      the function getArrayFromFile(filename)

    e.g.
        from helper import writeArrayToFile
        exampleArray = generateArrayOfLatinCubes(3)
        writeArrayToFile(exampleArray, "latinCubesOfSizethree")

getArrayFromFile(filename)
    - To call function, import the function from the file named "helper"
        - "from helper import getArrayFromFile"
    - Then for the first parameter, filename, you enter the name of the file
      you wish to retrieve. 

     e.g.
        from helper import getArrayFromFile
        exampleArray = getArrayFromFile("latinCubesOfSizethree")

"""


def writeArrayToFile(variable, filename):
    array = np.array(variable, dtype=object)
    file = open(f'SavedVariables/{filename}', "wb")
    np.save(file, array)
    file.close


def getArrayFromFile(filename):
    file = open(f'SavedVariables/{filename}', "rb")
    array = np.load(file, allow_pickle=True)
    array = array.tolist()
    return array
