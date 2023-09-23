# declaring vector constants
# where x[0] = a11 and x[1]
r = [-1, -2]
s = [-3, 3]
u = [2, -1]
v = [3, 1]
w = [1, 3]

# declaring constants
FILE_PATH = "C:/UCCS/CS2300/ProgAssignment1/programmingAssignment1/assignmentFiles/"


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


def dot_product(a, b):
    temp1 = (float(a[0]) * float(b[0]))
    temp2 = (float(a[1]) * float(b[1]))

    return_value = temp1 + temp2

    return return_value


print(
    "\n======================================================================================================================================================\n"
    "This program performs the dot product on two vectors that you choose | A dot B = C \n==================================================="
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
outgoing_file = "johara_p5_out"
temp_str = outgoing_file + user_a
temp_str = temp_str + user_b
output_filename = temp_str + ".txt"

output_file_path = FILE_PATH + output_filename

result = dot_product(vector_a, vector_b)

print("\nThe result is:", result)

with open(output_file_path, "w") as file:
    file.write(str(result))
