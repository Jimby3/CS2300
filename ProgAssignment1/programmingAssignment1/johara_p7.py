import numpy as np
import numpy.ma

# declaring vector constants
# where x[0] = a11 and x[1]
r = [-1, -2]
s = [-3, 3]
u = [2, -1]
v = [3, 1]
w = [1, 3]

# declaring constants
FILE_PATH = "C:/UCCS/CS2300/ProgAssignment1/programmingAssignment1/assignmentFiles/"


def write_matrix_to_file(file_path, matrix):
    with open(file_path, "w") as file:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                file.write(str(matrix[i][j]))
                file.write(" ")

            file.write("\n")


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


def choose_vector(user_input):
    return_vector = []

    if user_input == "r":
        return_vector = r

    elif user_input == "s":
        return_vector = s

    elif user_input == "u":
        return_vector = u

    elif user_input == "v":
        return_vector = v

    elif user_input == "w":
        return_vector = w

    else:
        print("Invalid Vector Letter. Please re-run application.")
        quit()

    return return_vector


print(
    "\n======================================================================================================================================================\n"
    "This program performs the dot product on two vectors that you choose (Using External Libraries | A dot B = C \n==================================================="
    "===================================================================================================\n")

print("Here are the vectors:")

print("r = [-1]  s = [-3]  u = [ 2] v = [3]  w = [1]\n"
      "    [-2]      [ 3]      [-1]     [1]      [3]\n\n")

print("Which vector do you want to be vector A? (Ex: r)")
user_a = input(":")

print("\nWhich vector do you want to be vector B? (Ex: s)")
user_b = input(":")

vector_a = choose_vector(user_a)
vector_b = choose_vector(user_b)

# making output file
outgoing_file = "johara_p7_outD"
temp_str = outgoing_file + user_a
temp_str = temp_str + user_b
output_filename = temp_str + ".txt"

output_file_path = FILE_PATH + output_filename

dp = np.dot(vector_a, vector_b)

with open(output_file_path, "w") as file:
    file.write(str(dp))

# transpose

print(
    "\n============================================================================================================================\n"
    "                 This program takes in a matrix and transposes it (Using External Libraries)\n==================================================="
    "=========================================================================\n")

print("Which matrix file do you want to be Matrix A? (Ex. Mat1)")
user_a = input(":")

outgoing_file = "johara_p7_matT"
temp_str = outgoing_file + user_a[-1]
output_filename = temp_str + ".txt"

file_a = ""

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

file_a_path = FILE_PATH + file_a
output_filepath = FILE_PATH + output_filename

matrix_a = read_matrix_from_file(file_a_path)

print("\nMatrix A:")
print(matrix_a)

trans_matrix = numpy.ma.transpose(matrix_a)

print("\nMatrix A(Transposed):")
print(trans_matrix)

write_matrix_to_file(output_filepath, trans_matrix)
