# creat a list
# Define two matrices as nested lists
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

# Initialize an empty result matrix
result_matrix = []

# Perform matrix addition
for i in range(len(matrix1)):
    row = []  # Initialize a row for the result matrix
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j] + matrix2[i][j])  # Add corresponding elements
    result_matrix.append(row)  # Append the row to the result matrix

# Print the result matrix (matrix addition)
for row in result_matrix:
    print(row)
