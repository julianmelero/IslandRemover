from test_cases import getMatrix
from islands import removeIslands

from sys import argv
if len(argv) != 2:
    exit(1)
level = argv[1]
matrix = getMatrix(level)

without_islands = removeIslands(matrix)
if without_islands != None:
    for row in without_islands:
        print(row)