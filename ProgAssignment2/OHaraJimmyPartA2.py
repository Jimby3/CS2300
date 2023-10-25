import numpy as np

FILE_PATH = "C:/UCCS/CS2300/ProgAssignment2/input-A21.txt"
FILE_PATH2 = "C:/UCCS/CS2300/ProgAssignment2/input-A22.txt"

# A 2.1
print("\n\n=================================== A2.1 ===================================\n")

char_array = []

# taking in num string from file set by path above^
with open(FILE_PATH, "r") as file:
    line = file.readline()

    for num in line:
        char_array.append(num)

print(char_array)

# vars for for loop
encrypted_array = []
i = 0

# for each char in array convert from list of chars -> int -> hex and add to list
for char in char_array:
    # getting the last two values of the hex char
    unicode = (hex(ord(char))[2:])

    # turning hex into decimal using base 16
    decimal_value = int(unicode, 16)

    encrypted_array.append(decimal_value)

print("Array of Encrypted Decimals: " + str(encrypted_array))

# A1.1

matrix_a = np.array([[1, -1, -1, 1],
                     [2, -3, -5, 4],
                     [-2, -1, -2, 2],
                     [3, -3, -1, 2]])

matrix_a_inverse = np.array([[6, -1, 0, -1],
                             [22, -4, 1, -4],
                             [14, -3, 1, -2],
                             [31, -6, 2, -5]])

print("\nInvertible Matrix A")
print(matrix_a)

matrix_b_transpose = []
index = 0
columns = []

# creating a Nx4 array to then transpose to get correct way
for num in encrypted_array:

    columns.append(num)

    # once a column has four rows, append it to the matrix
    if len(columns) == 4:
        matrix_b_transpose.append(columns)
        columns = []

# after going through all nums, if the last column is not full, add 0's till 4
while len(columns) < 4:
    columns.append(0)

matrix_b_transpose.append(columns)

matrix_b = np.transpose(np.array(matrix_b_transpose))

print("\n4x" + str(len(matrix_b[0])) + " Matrix from plaintext:")
print(matrix_b)

# A 1.3

# multiplying matrices
matrix_c = np.matmul(matrix_a, matrix_b)

print("\nResulting matrix C that is encrypted:")
print(matrix_c)

print("\nInverse Matrix A:\n " + str(matrix_a_inverse) + "\n")

# A2.2
print("\n=================================== A2.2 ===================================\n")

linear_sequence_array = []

with open(FILE_PATH2, "r") as file:
    line = file.read()
    numbers_str = line.split()
    numbers = []

    for num in numbers_str:
        linear_sequence_array.append(num)

print(linear_sequence_array)

print("\nInvertible Matrix A")
print(matrix_a)

matrix_b_transpose = []
index = 0
columns = []

# creating a Nx4 array to then transpose to get correct way
for num in encrypted_array:

    columns.append(num)

    # once a column has four rows, append it to the matrix
    if len(columns) == 4:
        matrix_b_transpose.append(columns)
        columns = []

# after going through all nums, if the last column is not full, add 0's till 4
while len(columns) < 4:
    columns.append(0)

matrix_b_transpose.append(columns)

matrix_b = np.transpose(np.array(matrix_b_transpose))

print("\n4x" + str(len(matrix_b[0])) + " Matrix from plaintext:")
print(matrix_b)

# A 1.3

# multiplying matrices
matrix_c = np.matmul(matrix_a, matrix_b)

print("\nCypher'd Matrix C:")
print(matrix_c)

print("\nMultiplying Matrix C by Decoding Matrix (inverse of A):")
decoded_matrix = np.matmul(matrix_a_inverse, matrix_c)
print(decoded_matrix)

print("\nPutting values into an array to get decoded message:")

decoded_matrix = np.transpose(decoded_matrix)

decoded_sequence = []

for i in range(len(decoded_matrix)):
    for num in decoded_matrix[i]:
        decoded_sequence.append(num)

print(decoded_sequence)

print("\nGetting decoded plaintext by converting numbs to chars:")

char_array = []
for num in decoded_sequence:
    char = chr(int(num))
    char_array.append(char)

print(char_array)

print("\nLastly, turning the char array into a string containing the plaintext:")

plaintext = ''.join(char_array)
print(plaintext)

