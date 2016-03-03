import numpy as np

# First system
# 4x1 - 1x2 + 2x3 + 3x4 = 40
# -2x2 + 7x3 - 4x4 = -7
# 6x3 + 5x4 = 4
# 3x4 = 6

a = np.array([[4, -1, 2, 3], [0, -2, 7, -4], [0, 0, 6, 5], [0, 0, 0, 3]])
b = np.array([20, -7, 4, 6])
x = np.linalg.solve(a, b)

print("First System")
for i in range(len(x)):
    print("X" + str(i) + " = " + str(x[i]))

print("The other systems had infinite or no solution")

