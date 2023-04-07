def matrix_transpose(matrix):

    tm = [[matrix[n][m] for n in range(len(matrix))] for m in range(len(matrix[0]))]
    return tm


matrix_initial = [[2, 1, 3], [3, 1, 5]]

matrix_transposed = matrix_transpose(matrix_initial)

matrix_rows_i = len(matrix_initial)
matrix_columns_i = len(matrix_initial[0])

matrix_rows_t = len(matrix_transposed)
matrix_columns_t = len(matrix_transposed[0])

print(f"\nMatrix transposed: {matrix_transposed}\n")
print(f"Transposed matrix dimension:\nmatrix rows: {matrix_rows_t}, matrix columns: {matrix_columns_t}\n") 
print(f"Initial matrix dimension:\nmatrix rows: {matrix_rows_i}, matrix columns: {matrix_columns_i}\n")