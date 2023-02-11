import numpy as np

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



def isCube(cube):
    newCube = np.array(cube)
    return len(newCube.shape) == 3

def printToLatexVirtualNAlegbraSize3():

    file = open("Tribrackets/VirtualNAlgebrasSizeThree", "rb")
    arrayOfVirtualNAlgebrasSizeThree = np.load(file, allow_pickle=True)
    arrayOfVirtualNAlgebrasSizeThree = arrayOfVirtualNAlgebrasSizeThree.tolist()

    print()
    print('\\begin{align*}')
    print()
    for element in arrayOfVirtualNAlgebrasSizeThree:
        for cube in element:
            if isCube(cube):
                for square in cube:
                    print("\\left[\\begin{array}{rrr}")
                    for row in square:
                        for item in row:
                            if(item != row[len(row)-1]):
                                print(item, end="&")
                            else:
                                print(item, end="")
                        if(row != square[len(square)-1]):
                            print('\\\\')
                    if(square != cube[len(cube)-1]):
                        print("\n\\end{array}\\right],")
                    else:
                        print("\n\\end{array}\\right]\\\\")
            else:
                print("\\left[\\begin{array}{rrr}")
                for row in cube:
                    for item in row:
                        if(item != row[len(row)-1]):
                            print(item, end="&")
                        else:
                            print(item, end="")
                    if(row != cube[len(cube)-1]):
                        print("\\\\")
                    else: 
                        print()
                print("\\end{array}\\right]")
            print()
            #     # else:
            #         # print(square)
            #     print()
            # print("DONE")
            # print(cube)
    print("\\end{align*}")


def printToLatexNAlgebrasSize3():
    file = open("Tribrackets/NAlgebrasSizeThree", "rb")
    arrayOfNAlgebrasSizeThree = np.load(file, allow_pickle=True)
    arrayOfNAlgebrasSizeThree = arrayOfNAlgebrasSizeThree.tolist()

    print()
    print('\\begin{align*}')
    print()
    for element in arrayOfNAlgebrasSizeThree:
        for cube in element:
            if isCube(cube):
                for square in cube:
                    print("\\left[\\begin{array}{rrr}")
                    for row in square:
                        for item in row:
                            if(item != row[len(row)-1]):
                                print(item, end="&")
                            else:
                                print(item, end="")
                        if(row != square[len(square)-1]):
                            print('\\\\')
                    if(square != cube[len(cube)-1]):
                        print("\n\\end{array}\\right],")
                    else:
                        print("\n\\end{array}\\right]\\\\")
            else:
                print("\\left[\\begin{array}{rrr}")
                for row in cube:
                    for item in row:
                        if(item != row[len(row)-1]):
                            print(item, end="&")
                        else:
                            print(item, end="")
                    if(row != cube[len(cube)-1]):
                        print("\\\\")
                    else: 
                        print()
                print("\\end{array}\\right]")
            print()
          
    print("\\end{align*}")

def printToLatexVirtualTribracketsSize3():
    # file = open("Tribrackets/VirtualTribracketsSizeThree", "rb")
    # arrayOfVirtualTribracketsSizeThree = np.load(file, allow_pickle=True)
    # arrayOfVirtualTribracketsSizeThree = arrayOfVirtualTribracketsSizeThree.tolist()

    file = open("Tribrackets/TribracketsSizeThree", "rb")
    arrayOfTribrackets = np.load(file, allow_pickle=True)
    arrayOfTribrackets = arrayOfTribrackets.tolist()
    print()
    print('\\begin{align*}')
    print()
    for element in arrayOfTribrackets:
        print("\\\\")
        # print()
        for cube in element:
            if isCube(cube):
                for square in cube:
                    print("\\left[\\begin{array}{rrr}")
                    for row in square:
                        for item in row:
                            if(item != row[len(row)-1]):
                                print(item, end="&")
                            else:
                                print(item, end="")
                        if(row != square[len(square)-1]):
                            print('\\\\')
                    if(square != cube[len(cube)-1]):
                        print("\n\\end{array}\\right],")
                    else:
                        print("\n\\end{array}\\right]\\\\")
            else:
                print("\\left[\\begin{array}{rrr}")
                for row in cube:
                    for item in row:
                        if(item != row[len(row)-1]):
                            print(item, end="&")
                        else:
                            print(item, end="")
                    if(row != cube[len(cube)-1]):
                        print("\\\\")
                    else: 
                        print()
                print("\\end{array}\\right]")
            print()
          
    print("\\end{align*}")

# printToLatexVirtualNAlegbraSize3()
# printToLatexNAlgebrasSize3()
# printToLatexVirtualTribracketsSize3()


    