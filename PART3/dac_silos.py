import random

def do_stuff(matrix, point):
    if len(matrix) <= 2:
        return populate_quarter_with_number(matrix, random.randint(1, 9))

    # Split the matrix into quarters
    quarter1, quarter2, quarter3, quarter4 = split_into_quarters(matrix)
    
    quarter1 = do_stuff(quarter1, point)
    quarter2 = do_stuff(quarter2, point)
    quarter3 = do_stuff(quarter3, point)
    quarter4 = do_stuff(quarter4, point)

    # Concatenate the quarters back into a single matrix
    full_matrix = []
    size = len(matrix)
    half_size = size // 2
    
    # Concatenate the first two quarters into the first half of the matrix
    for i in range(half_size):
        full_matrix.append(quarter1[i] + quarter2[i])
        
    # Concatenate the last two quarters into the second half of the matrix
    for i in range(half_size):
        full_matrix.append(quarter3[i] + quarter4[i])

    # Set the most inner 4 cells to 0
    full_matrix[half_size - 1][half_size - 1] = 0
    full_matrix[half_size - 1][half_size] = 0
    full_matrix[half_size][half_size - 1] = 0
    full_matrix[half_size][half_size] = 0
    
    return full_matrix
    
def populate_quarter_with_number(quarter, quarter_number):
    """
    Function to populate a quarter matrix with its number.
    
    Parameters:
        quarter (list of lists): The quarter matrix represented as a list of lists.
        quarter_number (int): The number of the quarter.
        
    Returns:
        list of lists: The modified quarter matrix with its number populated.
    """
    size = len(quarter)
    for i in range(size):
        for j in range(size):
            quarter[i][j] = quarter_number
    return quarter
    
    
def split_into_quarters(matrix):
    """
    Function to split a matrix into four quarters.
    
    Parameters:
        matrix (list of lists): The matrix represented as a list of lists.
        
    Returns:
        tuple: A tuple containing four quarters of the matrix.
    """
    size = len(matrix)
    half_size = size // 2
    
    quarter1 = [row[:half_size] for row in matrix[:half_size]]
    quarter2 = [row[half_size:] for row in matrix[:half_size]]
    quarter3 = [row[:half_size] for row in matrix[half_size:]]
    quarter4 = [row[half_size:] for row in matrix[half_size:]]
    
    return quarter1, quarter2, quarter3, quarter4

# Example usage:
matrix_size = 2
matrix = [[0] * matrix_size for _ in range(matrix_size)]  # Initialize an 8x8 matrix with zeros
modified_matrix = do_stuff(matrix, (0,0))

# Print the modified matrix
for row in modified_matrix:
    print(row)
