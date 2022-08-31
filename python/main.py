"""
Technical interview
"""
from sys import argv

from test_cases import getMatrix
from islands import remove_islands

if len(argv) != 2:
    exit(1)
level = argv[1]
matrix = getMatrix(level)

without_islands = remove_islands(matrix)
for row in without_islands:
    print(row)
