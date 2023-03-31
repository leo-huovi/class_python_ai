import numpy as np

#Let's define the matrices using Numpy's matrix objects:
A = np.matrix('1 2; 3 4')
B = np.matrix('-1 1; 5 7')

#Methosd for calculating the determinant can be found in the linalg submodule:
A_det = np.linalg.det(A)
B_det = np.linalg.det(B)
print("A Determinant: ", A_det)
print("B Determinant: ", B_det)

#Dot product is a basic numpy method:
AB = np.dot(A, B)
AB_det = np.linalg.det(AB)
print("AB Determinant: ", AB_det, "\n----")

#Let's calculate the product:
A_and_B_det_product = A_det * B_det
print("The product of A's deteminant and B's determinant: ", A_and_B_det_product, "\n----")

print(np.round(AB_det), "is rounded up the same as", np.round(A_and_B_det_product))
