# function to write a matrix to a given filepath
def write_matrix_to_file(file_path, matrix):
    with open(file_path, "w") as file:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                file.write(str(matrix[i][j]))
                file.write(" ")

            file.write("\n")


FIRST_NAME = "Jimmy"
LAST_NAME = "OHara"

FIRST_LENGTH = FIRST_NAME.__len__()
LAST_LENGTH = LAST_NAME.__len__()

MATRIX3_ROWS = 2
MATRIX3_COLS = 4

MATRIX4_ROWS = 4
MATRIX4_COLS = 2

print("Jimmy = 5")
print("OHara = 5")
print()

matrix1 = [[0 for _ in range(LAST_LENGTH)] for _ in range(FIRST_LENGTH)]

matrix2 = [[0 for _ in range(FIRST_LENGTH)] for _ in range(LAST_LENGTH)]

matrix3 = [[0 for _ in range(4)] for _ in range(2)]

matrix4 = [[0 for _ in range(2)] for _ in range(4)]


# Matrix 1
value = 1

# columns
for j in range(LAST_LENGTH):
    # rows
    for i in range(FIRST_LENGTH):
        matrix1[i][j] = value
        value += 1


# Matrix 2
value = 2

# rows
for i in range(FIRST_LENGTH):
    # columns
    for j in range(LAST_LENGTH):
        matrix2[i][j] = value
        value += 3


# Matrix 3

value = 10

# columns
for j in range(4):
    # rows
    for i in range(2):
        matrix3[i][j] = value
        value -= 2


# Matrix 4

value = -6

# rows
for i in range(4):
    # columns
    for j in range(2):
        matrix4[i][j] = value
        value += 1.5


file_path = "C:/UCCS/CS2300/ProgAssignment1/programmingAssignment1/assignmentFiles/johara_mat1.txt"
write_matrix_to_file(file_path, matrix1)


file_path = "C:/UCCS/CS2300/ProgAssignment1/programmingAssignment1/assignmentFiles/johara_mat2.txt"
write_matrix_to_file(file_path, matrix2)


file_path = "C:/UCCS/CS2300/ProgAssignment1/programmingAssignment1/assignmentFiles/johara_mat3.txt"
write_matrix_to_file(file_path, matrix3)


file_path = "C:/UCCS/CS2300/ProgAssignment1/programmingAssignment1/assignmentFiles/johara_mat4.txt"
write_matrix_to_file(file_path, matrix4)