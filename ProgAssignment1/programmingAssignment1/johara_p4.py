import numpy as np
import numpy.ma


def read_matrix_from_file(file_path):
    with open(file_path, "r") as file:

        end = False
        temp_array = []

        while end != True:

            line = file.readline()

            if line == "":
                end = True
            else:

                numbers_str = line.strip().split()

                temp_array.append(numbers_str)

        return temp_array


# function to write a matrix to a given filepath
def write_matrix_to_file(file_path, matrix):
    with open(file_path, "w") as file:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                file.write(str(matrix[i][j]))
                file.write(" ")

            file.write("\n")


# Script

FILE_PATH = "C:/UCCS/CS2300/ProgAssignment1/programmingAssignment1/assignmentFiles/"

print(
    "\n======================================================================================================================================================\n"
    "This program takes in two input files of matrices and adds them together | matrix_a + matrix_b = Output\n==================================================="
    "===================================================================================================\n")

print("Which matrix file do you want to be Matrix A? (Ex. Mat1)")
user_a = input(":")

print("\nWhich matrix file do you want to be Matrix B? (Ex. Mat3)")
user_b = input(":")

outgoing_file = "johara_p4_outA"
temp_str = outgoing_file + user_a[-1]
temp_str = temp_str + user_b[-1]
output_filename = temp_str + ".txt"

file_a = ""
file_b = ""

# determining file for A
if user_a == "Mat1":
    file_a = "johara_mat1.txt"

elif user_a == "Mat2":
    file_a = "johara_mat2.txt"

elif user_a == "Mat3":
    file_a = "johara_mat3.txt"

elif user_a == "Mat4":
    file_a = "johara_mat4.txt"

else:
    print("\nYou have entered a non-existant file (Please enter in the form of : \"Mat1\")\n\nStopping Program...\n")
    quit()

# determining file for B
if user_b == "Mat1":
    file_b = "johara_mat1.txt"

elif user_b == "Mat2":
    file_b = "johara_mat2.txt"

elif user_b == "Mat3":
    file_b = "johara_mat3.txt"

elif user_b == "Mat4":
    file_b = "johara_mat4.txt"

else:
    print("\nYou have entered a non-existant file (Please enter in the form of : \"Mat1\")\n\nStopping Program...\n")
    quit()

# reading matrix from file A
file_a_path = FILE_PATH + file_a
file_b_path = FILE_PATH + file_b
output_filepath = FILE_PATH + output_filename

matrix_a = read_matrix_from_file(file_a_path)
matrix_b = read_matrix_from_file(file_b_path)

print("\nMatrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

if matrix_a[0].__len__() != matrix_b[0].__len__() or matrix_a.__len__() != matrix_b.__len__():
    # cannot add, dont match (Ex 5x1 + 5x2)
    print("\n==========================\nCannot add, do not match\n==========================")
else:

    # adding matrix
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)

    matrix_a = matrix_a.astype(float)
    matrix_b = matrix_b.astype(float)

    resulting_matrix = np.add(matrix_a, matrix_b)

    write_matrix_to_file(output_filepath, resulting_matrix)

    print("\nResulting matrix C:")
    print(resulting_matrix)



print("\n======================================================================================================================================================\n"
      "This program takes in two input files of matrices and multiplies them together (Using External Libraries) | matrix_a + matrix_b = Output\n==================================================="
      "===================================================================================================\n")

print("Which matrix file do you want to be Matrix A? (Ex. Mat1)")
user_a = input(":")

print("\nWhich matrix file do you want to be Matrix B? (Ex. Mat3)")
user_b = input(":")

outgoing_file = "johara_p4_outM"
temp_str = outgoing_file + user_a[-1]
temp_str = temp_str + user_b[-1]
output_filename = temp_str + ".txt"

file_a = ""
file_b = ""

# determining file for A
if user_a == "Mat1":
    file_a = "johara_mat1.txt"

elif user_a == "Mat2":
    file_a = "johara_mat2.txt"

elif user_a == "Mat3":
    file_a = "johara_mat3.txt"

elif user_a == "Mat4":
    file_a = "johara_mat4.txt"

else:
    print("\nYou have entered a non-existant file (Please enter in the form of : \"Mat1\")\n\nStopping Program...\n")
    quit()

# determining file for B
if user_b == "Mat1":
    file_b = "johara_mat1.txt"

elif user_b == "Mat2":
    file_b = "johara_mat2.txt"

elif user_b == "Mat3":
    file_b = "johara_mat3.txt"

elif user_b == "Mat4":
    file_b = "johara_mat4.txt"

else:
    print("\nYou have entered a non-existant file (Please enter in the form of : \"Mat1\")\n\nStopping Program...\n")
    quit()


# reading matrix from file A
file_a_path = FILE_PATH + file_a
file_b_path = FILE_PATH + file_b
output_filepath = FILE_PATH + output_filename


matrix_a = read_matrix_from_file(file_a_path)
matrix_b = read_matrix_from_file(file_b_path)

print("\nMatrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

a_cols = len(matrix_a[0])
b_rows = len(matrix_b)


if a_cols != b_rows:
    # cannot multiply does not match (Ex 5x1 + 3x2, 1 != 3)
    print("\n==========================\ncannot multiply does not match | (Ex 5x1 + 3x2, 1 != 3\n==========================")

    print("\nShutting down...")
else:

    # multiplying matrices
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)

    matrix_a = matrix_a.astype(float)
    matrix_b = matrix_b.astype(float)

    resulting_matrix = np.dot(matrix_a, matrix_b)

    write_matrix_to_file(output_filepath, resulting_matrix)

    print("\nResulting matrix C:")
    print(resulting_matrix)

