# An Invariant of Virtual Trivalent Spatial Graphs

## Introduction
This Python program generates various types of mathematical structures, including exhaustively computed configurations of 
Latin Squares, Latin Cubes, Tribrackets, and partial Latin Squares of dimensions 3x3 and 4x4. The program also includes calculations for unique 
3x3 Niebrzydowski algebra and 3x3 virtual Niebrzydowski algebra, and computations for all distinct partially defined virtual tribrackets and 
Niebrzydowski algebras of size 3.

## Requirements
* Python 3.6 or higher
* NumPy library

## Installation
1. Clone or download the repository to your local machine.
2. Install the NumPy library by running the following command in your terminal:

```
pip install numpy
```

## Usage
In `main.py` there is a function to create a text file will all information of order N. The information will display how many variations/pairs exist of each type. 
```
def writeInformationOfOrderNToFile(size, filename):
```
An example call would look like: 
```
if __name__ == "__main__":
    writeInformationOfOrderNToFile(3, "OrderThree")
```
This would output a text file: `OrderThree.txt` in the root directory of the project. There you can open the file and look at the generated information. Bear in mind that this may take a long period of time since the number of each generated pairings are very large.
