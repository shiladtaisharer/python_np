import numpy as np
import matplotlib.pyplot as plt

# Create a matrix of random numbers
matrix = np.random.rand(3, 3)

# Display the created matrix
print("Original Matrix:")
print(matrix)

# Calculate the determinant of the matrix
determinant = np.linalg.det(matrix)
print("\nDeterminant of the Matrix:", determinant)

# Calculate the inverse matrix
inverse_matrix = np.linalg.inv(matrix)
print("\nInverse of the Matrix:")
print(inverse_matrix)

# Generate a vector
vector = np.array([1, 2, 3])

# Multiply the matrix by the vector
result_vector = np.dot(matrix, vector)
print("\nResult of Matrix-Vector Multiplication:")
print(result_vector)

# Generate data for the plot
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the functions
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('Sine and Cosine Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
