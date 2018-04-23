import numpy as np, math

#1. Create a 1d array M with values ranging for 2 to 26 and print M
a = np.arange(2, 27, 1)
print(a)
print()

#2. Reshape M as a 5*5 matrix and print M.
M = a.reshape(5, 5)
print(M)
print()

#3. Set the value of "inner" elements of the matrix M to 0 and print M.
M[1:-1, 1:-1] = 0
print(M)
print()

#4. Assign M^2 to the M and print M.
print(M @ M)
print()

#5. Let's call the first row of the matrix M a vector v. Calculate the magnitude
#   of the vector v and print it.
M = M @ M
v = M[0]
x = v@v
print(math.sqrt(x))
print()
