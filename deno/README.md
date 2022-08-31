Given some matrix of M x N dimensions filled with 1 or 0:

Complete the file islands.py with the function removeIslands that should return a matrix without islands.

We define an island as a 1 that cannot be connected horizontally or vertically with a group of 1's that reach the matrix border.

To test the solution just run ./check_solution.sh that will pass 5 different matrix and check if the output is correct or not (remember, blank is good).

Fork this to a public repository and send an email to rsanchez@homsa.es when finished with the repo link.

For example:

1 - Given this matrix.

    [1, 0, 1, 0, 0]
    [0, 1, 0, 1, 1]
    [0, 1, 0, 1, 0]
    [1, 0, 1, 1, 0]
    [1, 0, 0, 1, 0]

1 - Should return this matrix.

    [1, 0, 1, 0, 0]
    [0, 0, 0, 1, 1]
    [0, 0, 0, 1, 0]
    [1, 0, 1, 1, 0]
    [1, 0, 0, 1, 0]

2 - Given this matrix.

    [1, 0, 0, 0, 0, 0]
    [0, 1, 0, 1, 1, 1]
    [0, 0, 1, 0, 1, 0]
    [1, 1, 0, 0, 1, 0]
    [1, 0, 1, 1, 0, 0]
    [1, 0, 0, 0, 0, 1]

2 - Should return this matrix.

    [1, 0, 0, 0, 0, 0]
    [0, 0, 0, 1, 1, 1]
    [0, 0, 0, 0, 1, 0]
    [1, 1, 0, 0, 1, 0]
    [1, 0, 0, 0, 0, 0]
    [1, 0, 0, 0, 0, 1]
