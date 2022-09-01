"""
Module with islands related functions
"""
from typing import List

def is_border(n_col, n_fila,matrix):    
    # Está al borde la matriz    
    """ [0][0] 
    [0][4] 
    [4][0] 
    [4][4]
    Si la columna es la 0 o la última y es la primera ó última fila estoy en un borde
    n_col == 0 or n_col == n_filas
    """    
    n_filas = len(matrix) - 1

    if( (n_col == 0 or n_col == n_filas) or (n_fila == 0 or n_fila == n_filas)):
        return True
    else:
        return False


def get_round_numbers(n_fila,n_columna,matrix):        
    border = is_border(n_columna, n_fila,matrix)
    if(border == False):        
        left = matrix[n_fila][n_columna - 1]
        right = matrix[n_fila][n_columna + 1]
        up = matrix[n_fila- 1][n_columna]       
        down = matrix[n_fila+1][n_columna]        
        return left,right,up,down
    else:
        return None

def is_one(left,right,up,down):
    if (left == 1):
        return "left"
    elif(right == 1):
        return "right"
    elif(up == 1):
        return "up"
    elif(down == 1 ):
        return "down"
    else:
        return None

def convert_index_to_0(n_fila, n_col, matrix):
    matrix[n_fila][n_col] = 0

def change_coord(n_fila,n_columna, dir):
    if dir=="left":
        n_columna -=1
    elif dir=="right":
        n_columna +=1
    elif dir=="up":
        n_fila -=1
    else:
        n_fila +=1
    
    return n_fila,n_columna


def go_to_border(n_fila,n_columna,dir,matrix):    
    n_fila,n_columna = change_coord(n_fila,n_columna, dir)

    change = False

    if(n_fila < 0 or n_columna > (len(matrix) - 1)):
        return False

    if(is_border(n_columna,n_fila,matrix) == True and matrix[n_fila][n_columna] == 1):
            change = True
            return change
    elif(is_border(n_columna,n_fila,matrix) == True and matrix[n_fila][n_columna] == 0):
            return False        
    
    while(is_border(n_columna,n_fila,matrix) == False and matrix[n_fila][n_columna] == 1):
        n_fila,n_columna = change_coord(n_fila,n_columna, dir)           
        if(is_border(n_columna,n_fila,matrix) == True and matrix[n_fila][n_columna] == 1):
            change = True
    return change
            

def is_connected(n_fila,n_columna,matrix):
            if(matrix[n_fila][n_columna] == 1):
                if(get_round_numbers(n_fila,n_columna,matrix) != None):                    
                    if(go_to_border(n_fila,n_columna,'left',matrix)==False \
                         and go_to_border(n_fila,n_columna,'right',matrix)==False \
                            and go_to_border(n_fila,n_columna,'up',matrix)==False \
                                and go_to_border(n_fila,n_columna,'down',matrix)==False):
                        convert_index_to_0(n_fila,n_columna, matrix)

def remove_islands(matrix: List[List[int]]) -> List[List[int]]:
    """
    Function used to clear islands from given matrix
    """
    for n_fila,fila in enumerate(matrix):
        for n_columna,elemento in enumerate(fila):             
            is_connected(n_fila,n_columna,matrix)
    print(matrix)
    return matrix