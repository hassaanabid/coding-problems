"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
class Solution:
    """
        first row = 0, last row = n - 1
        
        90 degree clockwise rotation:
            row 0 -> col n-1
            row 1 -> col n-2
            ...
            row n-2 -> col 1
            row n-1 -> col 0
        
        # transpose of a matrix is a new matrix whose rows are the columns of the original
        # equvivalently: transpose of a matrix is an operator which flips a matrix over its diagonal
        tranpose of a matrix:
            row 0 -> col 0
            row 1 -> col 1
            ...
            row n-2 -> col n-2
            row n-1 -> col n-1
        
        hence, tranpose yields partial transformation
            reverse each row for full transformation
            i.e. col 0 -> col n-1 etc
        
        -> 90 degree anti-clockwise rotation
        1. rerverse rows
        2. tranpose matrix
    """
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for l in range (n - 1, 0, -2): # l is the length of the layer
            lo = (n-l) // 2 # start index of layer
            hi = lo + l # end index of layer
            for i in range(l):
                # indicies for 4-way swap
                top_left, top_right, bottom_right, bottom_left = \
                (lo, lo + i), (lo + i, hi), (hi, hi - i), (hi - i, lo)
                """
                assignments:
                    tmp = top_left
                    top_left = bottom_left
                    bottom_left = bottom_right
                    bottom_right = top_right
                    top_right = tmp
                """
                tmp = matrix[top_left[0]][top_left[1]]
                matrix[top_left[0]][top_left[1]]         = matrix[bottom_left[0]][bottom_left[1]]
                matrix[bottom_left[0]][bottom_left[1]]   = matrix[bottom_right[0]][bottom_right[1]]
                matrix[bottom_right[0]][bottom_right[1]] = matrix[top_right[0]][top_right[1]]
                matrix[top_right[0]][top_right[1]]       = tmp

                
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n=len(matrix)

        # loop over top-right half of diagonal and swap it with bottom-left half
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
                
        for i in range(n):
            matrix[i].reverse()