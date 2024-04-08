import random

class Node:
    def __init__(self, x, y):
        self.coord_x = x
        self.coord_y = y

def is_power_of_two(number):
    return number and (number & (number - 1)) == 0

def mostrar(campo):
    n = len(campo)
    for i in range(n):
        print("[", end='')
        for j in range(n):
            print(campo[i][j], end='')
            if (j < n-1):
                print(" ", end='')                
        print("]")

def paint_hectares(matrix, fake_silo: Node):
    random_number = random.randint(15,50)
    is_silo = False

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if(matrix[i][j] != 'x '):
                matrix[i][j] = random_number
            else:
                is_silo = True

    if(not is_silo):
        matrix[fake_silo.coord_x][fake_silo.coord_y] = 10

    return matrix

def recursive(matrix, fake_silo: Node):

    if (len(matrix) == 2):
        return  paint_hectares(matrix, fake_silo)
        
    quarter1, quarter2, quarter3, quarter4 = split_into_quarters(matrix)
    n = len(matrix)
    
    quarter1 = recursive(quarter1, Node(int(n/2)-1, int(n/2)-1))
    quarter2 = recursive(quarter2, Node(int(n/2)-1, 0))
    quarter3 = recursive(quarter3, Node(0, int(n/2)-1))
    quarter4 = recursive(quarter4, Node(0, 0))

    full_matrix = []
    size = len(matrix)
    half_size = size // 2
    
    for i in range(half_size):
        full_matrix.append(quarter1[i] + quarter2[i])
        
    for i in range(half_size):
        full_matrix.append(quarter3[i] + quarter4[i])

    
    return full_matrix

def split_into_quarters(matrix):
    size = len(matrix)
    half_size = size // 2
    
    quarter1 = [row[:half_size] for row in matrix[:half_size]]
    quarter2 = [row[half_size:] for row in matrix[:half_size]]
    quarter3 = [row[:half_size] for row in matrix[half_size:]]
    quarter4 = [row[half_size:] for row in matrix[half_size:]]
    
    return quarter1, quarter2, quarter3, quarter4

def main():
    n = 4
    x_silo = 1
    y_silo = 1

    if (not is_power_of_two(n) or n < 2):
        print("El valor de n ingresado debe ser potencia de 2 y mayor o igual a este.")
        return

    field = [[0]*n for _ in range(n)]
    field[x_silo][y_silo] = 'x '
    field = recursive(field, Node(0,0))

    mostrar(field)

if __name__ == "__main__":
    main()
