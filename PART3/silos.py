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
    random_number = random.randint(15, 50)
    foreground_color, background_color = get_random_color()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == fake_silo.coord_x and j == fake_silo.coord_y:
                continue
            matrix[i][j] = f"{background_color}{foreground_color}{random_number}\033[0m"
    matrix[fake_silo.coord_x][fake_silo.coord_y] = "\033[91m00\033[0m"

    return matrix

def get_random_color():
    foreground_colors = [
        "\033[92m",  # Green
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[97m",  # White
        "\033[32m",  # Dark green
        "\033[33m",  # Dark yellow
        "\033[34m",  # Dark blue
        "\033[37m",  # Light gray
        "\033[90m",  # Dark gray
    ]
    background_colors = [
        "\033[100m",  # Dark gray background
        "\033[41m",   # Dark red background
        "\033[42m",   # Dark green background
        "\033[43m",   # Dark yellow background
        "\033[44m",   # Dark blue background
        "\033[45m",   # Dark magenta background
        "\033[46m",   # Dark cyan background
    ]
    return random.choice(foreground_colors), random.choice(background_colors)


def recursive(matrix, fake_silo: Node):

    if (len(matrix) == 2):
        return  paint_hectares(matrix, fake_silo)
    
    quarter1, quarter2, quarter3, quarter4 = split_into_quarters(matrix)
    
    size = len(matrix)
    half_size = size // 2

    quarter_with_silo = get_quarter_containing_silo(matrix, fake_silo)
    
    if quarter_with_silo == 0:
        quarter1 = recursive(quarter1, fake_silo)
        quarter2 = recursive(quarter2, Node(half_size - 1, 0))
        quarter3 = recursive(quarter3, Node(0, half_size - 1))
        quarter4 = recursive(quarter4, Node(0, 0))
    elif quarter_with_silo == 1:
        quarter1 = recursive(quarter1, Node(half_size - 1, half_size - 1))
        quarter2 = recursive(quarter2, Node(fake_silo.coord_x, fake_silo.coord_y - half_size))
        quarter3 = recursive(quarter3, Node(0, half_size - 1))
        quarter4 = recursive(quarter4, Node(0, 0))
    elif quarter_with_silo == 2:
        quarter1 = recursive(quarter1, Node(half_size - 1, half_size - 1))
        quarter2 = recursive(quarter2, Node(half_size - 1, 0))
        quarter3 = recursive(quarter3, Node(fake_silo.coord_x - half_size, fake_silo.coord_y))
        quarter4 = recursive(quarter4, Node(0, 0))
    elif quarter_with_silo == 3:
        quarter1 = recursive(quarter1, Node(half_size - 1, half_size - 1))
        quarter2 = recursive(quarter2, Node(half_size - 1, 0))
        quarter3 = recursive(quarter3, Node(0, half_size - 1))
        quarter4 = recursive(quarter4, Node(fake_silo.coord_x - half_size, fake_silo.coord_y - half_size))

    full_matrix = []
    
    for i in range(half_size):
        full_matrix.append(quarter1[i] + quarter2[i])
        
    for i in range(half_size):
        full_matrix.append(quarter3[i] + quarter4[i])

    
    return full_matrix

def get_quarter_containing_silo(matrix, fake_silo: Node):
    size = len(matrix)
    half_size = size // 2
    row = fake_silo.coord_x
    col = fake_silo.coord_y
    
    if row < half_size:
        return 0 if col < half_size else 1
    else:
        return 2 if col < half_size else 3


def split_into_quarters(matrix):
    size = len(matrix)
    half_size = size // 2
    
    quarter1 = [row[:half_size] for row in matrix[:half_size]]
    quarter2 = [row[half_size:] for row in matrix[:half_size]]
    quarter3 = [row[:half_size] for row in matrix[half_size:]]
    quarter4 = [row[half_size:] for row in matrix[half_size:]]
    
    return quarter1, quarter2, quarter3, quarter4

def main():
    n = 16
    x_silo = 10
    y_silo = 12

    if (not is_power_of_two(n) or n < 2):
        print("El valor de n ingresado debe ser potencia de 2 y mayor o igual a este.")
        return

    field = [[0]*n for _ in range(n)]
    #field[x_silo][y_silo] = 'x '
    field = recursive(field, Node(x_silo, y_silo))
    # highlight the main silo
    field[x_silo][y_silo] = "\033[93m11\033[0m"
    mostrar(field)

if __name__ == "__main__":
    main()