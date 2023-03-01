import numpy as np

#Define the matrix:
A = np.matrix('1 2 3; 0 1 4; 5 6 0')

#Calculate the inverse:
inv_A = np.linalg.inv(A)

#Let's caculate the matrix products:

#AA^1
print( np.round(np.matmul(A, inv_A))  )


#A^1A
print( np.round(np.matmul(inv_A, A))  )
