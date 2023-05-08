import numpy as np

def isCube(cube):
    newCube = np.array(cube)
    return len(newCube.shape) == 3

def printToLatexVirtualNAlegbraSize3(arrayOfVirtualNAlgebrasSizeThree):
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
    print("\\end{align*}")


def printToLatexNAlgebrasSize3(arrayOfNAlgebrasSizeThree):
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

def printToLatexVirtualTribracketsSize3(arrayOfTribrackets):
    print()
    print('\\begin{align*}')
    print()
    for element in arrayOfTribrackets:
        print("\\\\")
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

if __name__ == "__main__":
    print("Here you would call these functions with the respective pairing (virtual tribrackets, virtual NAlgebras, NAlgebras)")


    