FIRST_NAME = "Jimmy"
LAST_NAME = "OHara"

FIRST_LENGTH = FIRST_NAME.__len__()
LAST_LENGTH = LAST_NAME.__len__()

print(LAST_LENGTH)

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

#rows
for i in range(4):
    # columns
    for j in range(2):
        matrix4[i][j] = value
        value += 1.5


file_path = "C:/Users/Jimev/Downloads/johara_mat1.txt"
with open(file_path, "w") as file:

    for i in range(matrix1.__len__())