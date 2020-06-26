import matrix_functions

#get_determinant_2X2()
print(matrix_functions.get_determinant_2X2([[1,6],[3,1]]))

#get_determinant_3X3()
print(matrix_functions.get_determinant_3X3([[1,8,6],[4,1,8],[9,5,1]]))

#get_matrix_vector_product()
print(matrix_functions.get_matrix_vector_product([[1,6,0],[6,1,4],[5,3,1]],[1,2,3]))

#get_matrix_matrix_addition()
print(matrix_functions.get_matrix_matrix_addition([[1,6,9],[8,1,7],[8,6,1]],[[1,2,3],[4,5,6],[7,8,9]]))

#get_matrix_matrix_subtraction()
print(matrix_functions.get_matrix_matrix_subtraction([[1,7,9],[6,1,7],[3,4,1]],[[1,2,3],[4,5,6],[7,8,9]]))

#get_matrix_matrix_product()
print(matrix_functions.get_matrix_matrix_product([[1,6,7],[4,1,3],[8,5,1]],[[1,2,3],[4,5,6],[7,8,9]]))

#get_matrix_matrix_quoitent()
print(matrix_functions.get_matrix_matrix_quoitent([[1,3,7],[4,1,8],[4,7,1]],[[1,2,3],[4,5,6],[7,8,9]]))

#get_matrix_matrix_exponent()
print(matrix_functions.get_matrix_matrix_exponent([[1,6,6],[7,1,2],[4,5,1]],[[1,2,3],[4,5,6],[7,8,9]]))

#get_matrix_matrix_modulus()
print(matrix_functions.get_matrix_matrix_modulus([[1,8,7],[5,1,4],[7,4,1]],[[1,2,3],[4,5,6],[7,8,9]]))

#get_matrix_matrix_composition()
print(matrix_functions.get_matrix_matrix_composition([[1,6,7],[6,1,6],[3,8,1]],[[1,2,3],[4,5,6],[7,8,9]]))

#get_solution_2X2()
print(matrix_functions.get_solution_2X2([[1,7],[4,1]],[1,1]))

#get_solution_3X3()
print(matrix_functions.get_solution_3X3([[1,3,6],[4,1,5],[6,4,1]],[1,1,1]))

#get_inverse_2X2()
print(matrix_functions.get_inverse_2X2([[1,0],[0,1]]))

#get_inverse_3X3()
print(matrix_functions.get_inverse_3X3([[1,0,5],[4,1,0],[0,4,1]]))
