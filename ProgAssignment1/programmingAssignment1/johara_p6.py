
FILE_PATH = "C:/UCCS/CS2300/ProgAssignment1/programmingAssignment1/assignmentFiles/"

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

def transpose_matrix(matrix):

    return_matrix = [[0 for _ in range(matrix_a[0].__len__())] for _ in range(matrix_a.__len__())]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            return_matrix[i][j] = matrix[j][i]



    return return_matrix

def write_matrix_to_file(file_path, matrix):
    with open(file_path, "w") as file:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                file.write(str(matrix[i][j]))
                file.write(" ")

            file.write("\n")

print("\n============================================================================================================================\n"
      "                 This program takes in a matrix and transposes it \n==================================================="
      "=========================================================================\n")

print("Which matrix file do you want to be Matrix A? (Ex. Mat1)")
user_a = input(":")



outgoing_file = "johara_p6_mat"
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

trans_matrix = transpose_matrix(matrix_a)

print("\nMatrix A(Transposed:")
print(trans_matrix)

write_matrix_to_file(output_filepath, trans_matrix)