
def get_determinant_2X2(matrix=[[1,2],[3,4]]):

    if type(matrix) is not list:
        print(" matrix must be of type array")
        return None

    for array in matrix:
        if not isinstance(array,list):
            print("All sublists of matrix must be arrays")
            return None

    for array in matrix:
        for char in array:
            if not isinstance(char,(int,float)):
                print("all entries in matrix must be numbers")
                return None
    
    if len(matrix) != 2:
        print("Matrix must be 2 by 2")
        return None
    
    for array in matrix:
        if len(array) != 2:
            print("All sublists of matrix must have length 2")
            return None
    
    determinant = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    return determinant

def get_determinant_3X3(matrix=[[1,2,3],[4,5,6],[7,8,9]]):

    if type(matrix) is not list:
        print(" matrix must be of type array")
        return None

    for array in matrix:
        if not isinstance(array,list):
            print("All sublists of matrix must be arrays")
            return None

    for array in matrix:
        for char in array:
            if not isinstance(char,(int,float)):
                print("all entries in matrix must be numbers")
                return None
            
    if len(matrix) != 3:
        print("Matrix must be 3 by 3")
        return None
    
    for array in matrix:
        if len(array) != 3:
            print("All sublists of matrix must have length 3")
            return None
        
    determinant = matrix[0][0]*matrix[1][1]*matrix[2][2]+\
    matrix[0][1]*matrix[1][2]*matrix[2][0]+\
    matrix[0][2]*matrix[1][0]*matrix[2][1]-\
    matrix[0][2]*matrix[1][1]*matrix[2][0]-\
    matrix[0][0]*matrix[1][2]*matrix[2][1]-\
    matrix[0][1]*matrix[1][0]*matrix[2][2]
    
    return determinant

def get_matrix_vector_product(matrix=[[1,2,3],[4,5,6],[7,8,9]],vector=[1,2,3]):

    if type(matrix) is not list:
        print(" matrix must be of type array")
        return None

    if type(vector) is not list:
        print("vector must be of type array")
        return None
    
    for array in matrix:
        if not isinstance(array,list):
            print("All sublists of matrix must be arrays")
            return None

    for array in matrix:
        for char in array:
            if not isinstance(char,(int,float)):
                print("all entries in matrix must be numbers")
                return None

    for char in vector:
        if not isinstance(char,(int,float)):
            print("all elements of vector must be numbers")
            return None
        
    for array in matrix:
        if len(array) !=  len(matrix):
            print("matrix must be square")
            return None
        
    if len(matrix) == 0 or len(vector) == 0:
        print("matrix and vector must not be empty")
        return None
    
    sumproduct=0;
    product_vector = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
			
            sumproduct+=matrix[row][col]*vector[col]
				
			
        product_vector.append(sumproduct)
        sumproduct=0
		
    return product_vector

def get_matrix_matrix_addition(matrix1=[[1,2,3],[4,5,6],[7,8,9]],matrix2=[[1,2,3],[4,5,6],[7,8,9]]):

    if (type(matrix1) is not list) or (type(matrix2) is not list):
        print("matrix1 and matrix2 must  be of type array")
        return None

    for array1 in matrix1:
        if not isinstance(array1,list):
            print("All sublists of matrix1 must be arrays")
            return None
        
    for array2 in matrix2:
        if not isinstance(array2,list):
            print("All sublists of matrix2 must be arrays")
            return None

    for array1 in matrix1:
        for char1 in array1:
            if not isinstance(char1,(int,float)):
                print("all entries in matrix1 must be numbers")
                return None
            
    for array2 in matrix2:
        for char2 in array2:
            if not isinstance(char2,(int,float)):
                print("all entries in matrix2 must be numbers")
                return None
            
    for array1 in matrix1:
        if len(array1) !=  len(matrix1):
            print("matrix1 must be square")
            return None

    for array2 in matrix2:
        if len(array2) !=  len(matrix2):
            print("matrix2 must be square")
            return None
        
    if len(matrix1) != len(matrix2):
        print("matrix1 and matrix2 must be the same size")
        return None

    if len(matrix1) == 0 or len(matrix2) == 0:
        print("matrix1 and matrix2 must not be empty")
        return None
    
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            print("matrix1 and matrix2 must be the same size")
            return None
        
    sum_entries=0
    sum_matrix=[]
    sum_vector=[]
		
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            sum_entries=matrix1[i][j]+matrix2[i][j]
            sum_vector.append(sum_entries)

			
        sum_matrix.append(sum_vector)
        sum_vector=[]
		
    return sum_matrix

def get_matrix_matrix_subtraction(matrix1=[[1,2,3],[4,5,6],[7,8,9]],matrix2=[[1,2,3],[4,5,6],[7,8,9]]):

    if (type(matrix1) is not list) or (type(matrix2) is not list):
        print("matrix1 and matrix2 must  be of type array")
        return None

    for array1 in matrix1:
        if not isinstance(array1,list):
            print("All sublists of matrix1 must be arrays")
            return None
        
    for array2 in matrix2:
        if not isinstance(array2,list):
            print("All sublists of matrix2 must be arrays")
            return None

    for array1 in matrix1:
        for char1 in array1:
            if not isinstance(char1,(int,float)):
                print("all entries in matrix1 must be numbers")
                return None
            
    for array2 in matrix2:
        for char2 in array2:
            if not isinstance(char2,(int,float)):
                print("all entries in matrix2 must be numbers")
                return None
            
    for array1 in matrix1:
        if len(array1) !=  len(matrix1):
            print("matrix1 must be square")
            return None

    for array2 in matrix2:
        if len(array2) !=  len(matrix2):
            print("matrix2 must be square")
            return None
        
    if len(matrix1) != len(matrix2):
        print("matrix1 and matrix2 must be the same size")
        return None

    if len(matrix1) == 0 or len(matrix2) == 0:
        print("matrix1 and matrix2 must not be empty")
        return None
    
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            print("matrix1 and matrix2 must be the same size")
            return None

    sum_entries=0
    sum_matrix=[]
    sum_vector=[]
		
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            sum_entries=matrix1[i][j]-matrix2[i][j]
            sum_vector.append(sum_entries)

			
        sum_matrix.append(sum_vector)
        sum_vector=[]
		
    return sum_matrix

def get_matrix_matrix_product(matrix1=[[1,2,3],[4,5,6],[7,8,9]],matrix2=[[1,2,3],[4,5,6],[7,8,9]]):

    if (type(matrix1) is not list) or (type(matrix2) is not list):
        print("matrix1 and matrix2 must  be of type array")
        return None

    for array1 in matrix1:
        if not isinstance(array1,list):
            print("All sublists of matrix1 must be arrays")
            return None
        
    for array2 in matrix2:
        if not isinstance(array2,list):
            print("All sublists of matrix2 must be arrays")
            return None

    for array1 in matrix1:
        for char1 in array1:
            if not isinstance(char1,(int,float)):
                print("all entries in matrix1 must be numbers")
                return None
            
    for array2 in matrix2:
        for char2 in array2:
            if not isinstance(char2,(int,float)):
                print("all entries in matrix2 must be numbers")
                return None
            
    for array1 in matrix1:
        if len(array1) !=  len(matrix1):
            print("matrix1 must be square")
            return None

    for array2 in matrix2:
        if len(array2) !=  len(matrix2):
            print("matrix2 must be square")
            return None
        
    if len(matrix1) != len(matrix2):
        print("matrix1 and matrix2 must be the same size")
        return None

    if len(matrix1) == 0 or len(matrix2) == 0:
        print("matrix1 and matrix2 must not be empty")
        return None
    
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            print("matrix1 and matrix2 must be the same size")
            return None

    product_entries=0
    product_matrix=[]
    product_vector=[]
		
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            product_entries=matrix1[i][j]*matrix2[i][j]
            product_vector.append(product_entries)

			
        product_matrix.append(product_vector)
        product_vector=[]
		
    return product_matrix

def get_matrix_matrix_quoitent(matrix1=[[1,2,3],[4,5,6],[7,8,9]],matrix2=[[1,2,3],[4,5,6],[7,8,9]]):

    if (type(matrix1) is not list) or (type(matrix2) is not list):
        print("matrix1 and matrix2 must  be of type array")
        return None

    for array1 in matrix1:
        if not isinstance(array1,list):
            print("All sublists of matrix1 must be arrays")
            return None
        
    for array2 in matrix2:
        if not isinstance(array2,list):
            print("All sublists of matrix2 must be arrays")
            return None

    for array1 in matrix1:
        for char1 in array1:
            if not isinstance(char1,(int,float)):
                print("all entries in matrix1 must be numbers")
                return None
            
    for array2 in matrix2:
        for char2 in array2:
            if not isinstance(char2,(int,float)):
                print("all entries in matrix2 must be numbers")
                return None
            
    for array1 in matrix1:
        if len(array1) !=  len(matrix1):
            print("matrix1 must be square")
            return None

    for array2 in matrix2:
        if len(array2) !=  len(matrix2):
            print("matrix2 must be square")
            return None
        
    if len(matrix1) != len(matrix2):
        print("matrix1 and matrix2 must be the same size")
        return None

    if len(matrix1) == 0 or len(matrix2) == 0:
        print("matrix1 and matrix2 must not be empty")
        return None
    
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            print("matrix1 and matrix2 must be the same size")
            return None

    product_entries=0
    product_matrix=[]
    product_vector=[]
		
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            product_entries=matrix1[i][j]/matrix2[i][j]
            product_vector.append(product_entries)

			
        product_matrix.append(product_vector)
        product_vector=[]
		
    return product_matrix

def get_matrix_matrix_exponent(matrix1=[[1,2,3],[4,5,6],[7,8,9]],matrix2=[[1,2,3],[4,5,6],[7,8,9]]):

    if (type(matrix1) is not list) or (type(matrix2) is not list):
        print("matrix1 and matrix2 must  be of type array")
        return None

    for array1 in matrix1:
        if not isinstance(array1,list):
            print("All sublists of matrix1 must be arrays")
            return None
        
    for array2 in matrix2:
        if not isinstance(array2,list):
            print("All sublists of matrix2 must be arrays")
            return None

    for array1 in matrix1:
        for char1 in array1:
            if not isinstance(char1,(int,float)):
                print("all entries in matrix1 must be numbers")
                return None
            
    for array2 in matrix2:
        for char2 in array2:
            if not isinstance(char2,(int,float)):
                print("all entries in matrix2 must be numbers")
                return None
            
    for array1 in matrix1:
        if len(array1) !=  len(matrix1):
            print("matrix1 must be square")
            return None

    for array2 in matrix2:
        if len(array2) !=  len(matrix2):
            print("matrix2 must be square")
            return None
        
    if len(matrix1) != len(matrix2):
        print("matrix1 and matrix2 must be the same size")
        return None

    if len(matrix1) == 0 or len(matrix2) == 0:
        print("matrix1 and matrix2 must not be empty")
        return None
    
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            print("matrix1 and matrix2 must be the same size")
            return None

    exponent_entries=0
    exponent_matrix=[]
    exponent_vector=[]
		
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            exponent_entries=matrix1[i][j]**matrix2[i][j]
            exponent_vector.append(exponent_entries)

			
        exponent_matrix.append(exponent_vector)
        exponent_vector=[]
		
    return exponent_matrix

def get_matrix_matrix_modulus(matrix1=[[1,2,3],[4,5,6],[7,8,9]],matrix2=[[1,2,3],[4,5,6],[7,8,9]]):

    if (type(matrix1) is not list) or (type(matrix2) is not list):
        print("matrix1 and matrix2 must  be of type array")
        return None

    for array1 in matrix1:
        if not isinstance(array1,list):
            print("All sublists of matrix1 must be arrays")
            return None
        
    for array2 in matrix2:
        if not isinstance(array2,list):
            print("All sublists of matrix2 must be arrays")
            return None

    for array1 in matrix1:
        for char1 in array1:
            if not isinstance(char1,(int,float)):
                print("all entries in matrix1 must be numbers")
                return None
            
    for array2 in matrix2:
        for char2 in array2:
            if not isinstance(char2,(int,float)):
                print("all entries in matrix2 must be numbers")
                return None
            
    for array1 in matrix1:
        if len(array1) !=  len(matrix1):
            print("matrix1 must be square")
            return None

    for array2 in matrix2:
        if len(array2) !=  len(matrix2):
            print("matrix2 must be square")
            return None
        
    if len(matrix1) != len(matrix2):
        print("matrix1 and matrix2 must be the same size")
        return None

    if len(matrix1) == 0 or len(matrix2) == 0:
        print("matrix1 and matrix2 must not be empty")
        return None
    
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            print("matrix1 and matrix2 must be the same size")
            return None

    modulus_entries=0
    modulus_matrix=[]
    modulus_vector=[]
		
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            modulus_entries=matrix1[i][j]%matrix2[i][j]
            modulus_vector.append(modulus_entries)

			
        modulus_matrix.append(modulus_vector)
        modulus_vector=[]
		
    return modulus_matrix

def get_matrix_matrix_composition(matrix1=[[1,2,3],[4,5,6],[7,8,9]], matrix2=[[1,2,3],[4,5,6],[7,8,9]]):

    if (type(matrix1) is not list) or (type(matrix2) is not list):
        print("matrix1 and matrix2 must  be of type array")
        return None

    for array1 in matrix1:
        if not isinstance(array1,list):
            print("All sublists of matrix1 must be arrays")
            return None
        
    for array2 in matrix2:
        if not isinstance(array2,list):
            print("All sublists of matrix2 must be arrays")
            return None

    for array1 in matrix1:
        for char1 in array1:
            if not isinstance(char1,(int,float)):
                print("all entries in matrix1 must be numbers")
                return None
            
    for array2 in matrix2:
        for char2 in array2:
            if not isinstance(char2,(int,float)):
                print("all entries in matrix2 must be numbers")
                return None
            
    for array1 in matrix1:
        if len(array1) !=  len(matrix1):
            print("matrix1 must be square")
            return None

    for array2 in matrix2:
        if len(array2) !=  len(matrix2):
            print("matrix2 must be square")
            return None
        
    if len(matrix1) != len(matrix2):
        print("matrix1 and matrix2 must be the same size")
        return None

    if len(matrix1) == 0 or len(matrix2) == 0:
        print("matrix1 and matrix2 must not be empty")
        return None
    
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            print("matrix1 and matrix2 must be the same size")
            return None

    sumproduct=0
    composition_matrix=[]
    composition_vector=[]

    for k in range(len(matrix2)):
        for i in range(len(matrix1)):
            for j in range(len(matrix2[i])):
                sumproduct+=matrix1[k][j]*matrix2[i][j]
				
			
            composition_vector.append(sumproduct)
            sumproduct=0
		
        composition_matrix.append(composition_vector)
        composition_vector=[]

    return composition_matrix

def get_solution_2X2(coeffecient_matrix=[[1,0],[0,1]],result_vector=[1,1]):

    if type(coeffecient_matrix) is not list:
        print("coeffecient_matrix must be of type array")
        return None

    if type(result_vector) is not list:
        print("result_vector must be of type array")
        return None
    
    for array in coeffecient_matrix:
        if not isinstance(array,list):
            print("All sublists of coeffecient_matrix must be arrays")
            return None

    for array in coeffecient_matrix:
        for char in array:
            if not isinstance(char,(int,float)):
                print("all entries in coeffecient_matrix must be numbers")
                return None

    for char in result_vector:
        if not isinstance(char,(int,float)):
            print("all elements of result_vector must be numbers")
            return None
        
    for array in coeffecient_matrix:
        if len(array) !=  len(coeffecient_matrix):
            print("coeffecient_matrix must be square")
            return None
        
    if len(coeffecient_matrix) !=2 or len(result_vector) !=2:
        print("coeffecient_matrix and result_vector must have length 2")
        return None
    
    new_coeffecient_matrix = []
    for row_vector in coeffecient_matrix:
        vector=[]
        for entry in row_vector:
            vector.append(entry)
        new_coeffecient_matrix.append(vector)
        
    coeffecient_det=get_determinant_2X2(new_coeffecient_matrix)

    new_coeffecient_matrix[0] = result_vector
    det_x=get_determinant_2X2(new_coeffecient_matrix)

    new_coeffecient_matrix[0] = coeffecient_matrix[0]
    new_coeffecient_matrix[1] = result_vector
    det_y=get_determinant_2X2(new_coeffecient_matrix)

    answer_vector=[]
    answer_vector.append(det_x/coeffecient_det)
    answer_vector.append(det_y/coeffecient_det)

    return answer_vector

def get_solution_3X3(coeffecient_matrix=[[1,0,0],[0,1,0],[0,0,1]],result_vector=[1,1,1]):

    if type(coeffecient_matrix) is not list:
        print("coeffecient_matrix must be of type array")
        return None

    if type(result_vector) is not list:
        print("result_vector must be of type array")
        return None
    
    for array in coeffecient_matrix:
        if not isinstance(array,list):
            print("All sublists of coeffecient_matrix must be arrays")
            return None

    for array in coeffecient_matrix:
        for char in array:
            if not isinstance(char,(int,float)):
                print("all entries in coeffecient_matrix must be numbers")
                return None

    for char in result_vector:
        if not isinstance(char,(int,float)):
            print("all elements of result_vector must be numbers")
            return None
        
    for array in coeffecient_matrix:
        if len(array) !=  len(coeffecient_matrix):
            print("coeffecient_matrix must be square")
            return None
        
    if len(coeffecient_matrix) !=3 or len(result_vector) !=3:
        print("coeffecient_matrix and result_vector must have length 3")
        return None

    new_coeffecient_matrix=[]
    for row_vector in coeffecient_matrix:
        vector=[]
        for entry in row_vector:
            vector.append(entry)
        new_coeffecient_matrix.append(vector)
        
    coeffecient_det=get_determinant_3X3(new_coeffecient_matrix)

    new_coeffecient_matrix[0] = result_vector
    det_x=get_determinant_3X3(new_coeffecient_matrix)

    new_coeffecient_matrix[0] = coeffecient_matrix[0]
    new_coeffecient_matrix[1] = result_vector
    det_y=get_determinant_3X3(new_coeffecient_matrix)

    new_coeffecient_matrix[1] = coeffecient_matrix[1]
    new_coeffecient_matrix[2]=result_vector
    det_z = get_determinant_3X3(new_coeffecient_matrix)
    
    answer_vector=[]
    answer_vector.append(det_x/coeffecient_det)
    answer_vector.append(det_y/coeffecient_det)
    answer_vector.append(det_z/coeffecient_det)
    
    return answer_vector

def get_inverse_2X2(matrix=[[1,0],[0,1]]):

    if type(matrix) is not list:
        print(" matrix must be of type array")
        return None

    for array in matrix:
        if not isinstance(array,list):
            print("All sublists of matrix must be arrays")
            return None

    for array in matrix:
        for char in array:
            if not isinstance(char,(int,float)):
                print("all entries in matrix must be numbers")
                return None
    
    if len(matrix) != 2:
        print("Matrix must be 2 by 2")
        return None
    
    for array in matrix:
        if len(array) != 2:
            print("All sublists of matrix must have length 2")
            return None
        
    inverse_matrix_row1 = get_solution_2X2(matrix,[1,0])
    inverse_matrix_row2 =  get_solution_2X2(matrix,[0,1])

    inverse_matrix=[]
    inverse_matrix.append(inverse_matrix_row1)
    inverse_matrix.append(inverse_matrix_row2)

    return inverse_matrix

def get_inverse_3X3(matrix=[[1,0,0],[0,1,0],[0,0,1]]):

    if type(matrix) is not list:
        print(" matrix must be of type array")
        return None

    for array in matrix:
        if not isinstance(array,list):
            print("All sublists of matrix must be arrays")
            return None

    for array in matrix:
        for char in array:
            if not isinstance(char,(int,float)):
                print("all entries in matrix must be numbers")
                return None
    
    if len(matrix) != 3:
        print("Matrix must be 3 by 3")
        return None
    
    for array in matrix:
        if len(array) != 3:
            print("All sublists of matrix must have length 3")
            return None
        
    inverse_matrix_row1 = get_solution_3X3(matrix,[1,0,0])
    inverse_matrix_row2 =  get_solution_3X3(matrix,[0,1,0])
    inverse_matrix_row3 =  get_solution_3X3(matrix,[0,0,1])

    inverse_matrix=[]
    inverse_matrix.append(inverse_matrix_row1)
    inverse_matrix.append(inverse_matrix_row2)
    inverse_matrix.append(inverse_matrix_row3)

    return inverse_matrix

    
    
