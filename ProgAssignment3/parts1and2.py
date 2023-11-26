import numpy as np
import matplotlib.pyplot as pyplot

#reads in a matrix from a file
def read_matrix_from_file(file_path):
    with open(file_path, "r") as file:

        end = False
        temp_array = []

        while end != True:

            line = file.readline()

            if line == "":
                end = True
            else:

                str_numbers_str = line.strip().split()

                numbers_str = [float(num) for num in str_numbers_str]

                temp_array.append(numbers_str)

        return temp_array


#part1

print("\n\n================== Part 1 ==================\n\n")

# setting constants and matrices
identity_matrix = np.array(read_matrix_from_file("C:/UCCS/CS2300/ProgAssignment3/Matrices/identityMatrix.txt"))
PATH_TO_MATRIX_D = "C:/UCCS/CS2300/ProgAssignment3/Matrices/matrixD.txt"
PATH_TO_MATRIX_E = "C:/UCCS/CS2300/ProgAssignment3/Matrices/matrixE.txt"

# getting matrix D from file
print("Reading in matrix D from: " + PATH_TO_MATRIX_D)
matrix_d = np.array(read_matrix_from_file(PATH_TO_MATRIX_D))

print("\nMatrix D:")
print(matrix_d)

# getting matrix E from file
print("\n\nReading in matrix E from: " + PATH_TO_MATRIX_E)
matrix_e = np.array(read_matrix_from_file(PATH_TO_MATRIX_E))

print("\nMatrix E:")
print(matrix_e)

# I - D
identity_subtracted_from = np.subtract(identity_matrix, matrix_d)
print("\n\nI - D:")
print(identity_subtracted_from)

# (I - D) inverse
inverse_i_minus_d = np.linalg.inv(identity_subtracted_from)
print("\n\nInverse of I - D:")
print(inverse_i_minus_d)

# output matrix
resulting_matrix = np.dot(inverse_i_minus_d, matrix_e)
print("\n\nOutput Matrix (inverse(I - D)E) [Rounded]: ")

rounded_resulting_matrix = np.round(resulting_matrix, 1)
print(rounded_resulting_matrix)

print("\n\n================== Part 2 ==================\n\n")

# constants
ORDERED_PAIRS_PATH = "C:/UCCS/CS2300/ProgAssignment3/Matrices/orderedPairs.txt"

# reading in ordered pairs as matrix
ordered_pair_matrix = np.array(read_matrix_from_file(ORDERED_PAIRS_PATH))
ordered_pair_matrix2 = np.array(read_matrix_from_file(ORDERED_PAIRS_PATH))

# setting up matrix x
matrix_x = np.fliplr(ordered_pair_matrix)

for i in range(len(matrix_x)):
    matrix_x[i][0] = 1

print("Matrix X: ")
print(matrix_x)

# setting up matrix y
matrix_y = ordered_pair_matrix2[:, 1]
matrix_y = matrix_y.reshape(-1 ,1)

print("\nMatrix Y: ")
print(matrix_y)

# setting up matx trans * matx

xtransx = np.dot(np.transpose(matrix_x), matrix_x)

print("\nX-transpose times X: ")
print(xtransx)

# setting up matx trans * maty

xtransy = np.dot(np.transpose(matrix_x), matrix_y)

print("\nX-transpose times Y: ")
print(xtransy)

# getting the coefficient matrix

coeff_matrix = np.dot(np.linalg.inv(xtransx),xtransy)

print("\nCoeff Matrix: ")
print(coeff_matrix)

# Getting linear equation

m = coeff_matrix[1][0]
b = coeff_matrix[0][0]

print("\nLinear Equation: ")
print("Y = " + str(round(b,1)) + " + " + str(round(m,1)) + "x")
linear_eqn_string = "Y = " + str(round(b, 1)) + " + " + str(round(m, 1)) + "x"


# graphing equation + points


x_values = []
y_values = []

# Read the file and extract ordered pairs
with open("C:/UCCS/CS2300/ProgAssignment3/Matrices/orderedPairs.txt", 'r') as file:

    for line in file:
        # Split each line into x and y values
        x, y = map(int, line.split())

        # Append values to the lists
        x_values.append(x)
        y_values.append(y)

x = np.linspace(0,50,100)
y = m * x + b

pyplot.scatter(x_values, y_values, color='red', marker='o', label="Coordinates")

pyplot.plot(x, y, label=linear_eqn_string)  # plot the linear equation
pyplot.xlabel('Price')
pyplot.ylabel('Monthly Sales')
pyplot.legend()  # display the legend with the equation
pyplot.grid(True)
pyplot.show()