import numpy as np

# B2.1

print("Please enter Flow Number 1:")
flow_num_1 = input()

print("Please enter Flow Number 2:")
flow_num_2 = input()

print("Please enter Flow Number 3:")
flow_num_3 = input()

print("Please enter Flow Number 4:")
flow_num_4 = input()

# ===== System of equations =====
# x1 = flow_num_4 + x4 || x1 - x4 = flow_num_4
# x2 = x1 - flow_num_3 || x1 - x2 = flow_num_3
# x3 = x2 + flow_num_2 || x3 - x2 = flow_num_2sc
# x4 = x3 - flow_num_1 || x3 - x4 = flow_num_1

# |  x1   0   0 -x4 | | x1 |    | flow_num_4 |
# |  x1 -x2   0   0 | | x2 | =  | flow_num_3 |
# |   0 -x2  x3   0 | | x3 |    | flow_num_2 |
# |   0   0  x3 -x4 | | x4 |    | flow_num_1 |

augmented_matrix = np.array([[1, -1, 0, 0, flow_num_3], [1, 0, 0, -1, flow_num_4], [0, -1, 1, 0, flow_num_2], [0, 0, 1, -1, flow_num_1]])

print(augmented_matrix)








