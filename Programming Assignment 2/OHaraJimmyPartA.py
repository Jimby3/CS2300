import numpy as np

# function to write a matrix to stdout



print("Please enter the message you want to encrypt:")
message = input(":")

# seperating input into array of chars
charArray = list(message)


# vars for for loop
encrypted_array = []
i = 0

# for each char in array convert from list of chars -> int -> hex and add to list
for char in charArray:
    # getting the last two values of the hex char
    unicode = (hex(ord(char))[2:])

    # turning hex into decimal using base 16
    decimal_value = int(unicode,16)

    encrypted_array.append(decimal_value)

print("Array of Encrypted Decimals: " + str(encrypted_array))



# A1.1

matrix_a = np.array([[1, -1, -2, 3],
                     [2, -3, -5, 4],
                     [-2, -1, -2, 2],
                     [3, -3, -1, 2]])



print("\nInvertible Matrix A")
print(matrix_a)

# A1.2 || Encrypting the message –matrix B:

# ----------> Question #1: Why does this plaintext matrix have to be made up of column vectors of 4 <-------------------
# elements?
# Because the matrix we chose to do the encrypting is a 4x4, and it has to be able to multiply by it to encrypt
# 4x(4) * (4)xN, the middle 2 nums must match


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

print("\n4x" + str(len(matrix_b[0])) + " Matrix from Encrypted Message:")
print(matrix_b)