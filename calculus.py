import math

def get_polynomial_value(num=1,coeffecients=[1]):

    if type(coeffecients) is not list:
        print("coeffecients must be of type array ")
        return None
        
    for char in coeffecients:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients must be numbers")
            return None

    if len(coeffecients) == 0:
        print("coeffecients cannot be empty ")
        return None
            
    exponents = []
    for exponent in range(len(coeffecients)-1,-1,-1):
        exponents.append(exponent)

    result=0
		
    for i in range(len(coeffecients)):
        result+=coeffecients[i]*num**exponents[i]
			
    return result
    
def get_rational_value(num=1,coeffecients1=[1],coeffecients2=[1]):

    if type(coeffecients1) is not list:
        print("coeffecient1 must be of type array ")
        return None
        
    if type(coeffecients2) is not list:
        print("coeffecient2 must be of type array ")
        return None
        
    for char in coeffecients1:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecient1 must be numbers")
            return None

    for char in coeffecients2:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecient2 must be numbers")
            return None
            
    if len(coeffecients1) == 0:
        print("coeffecients1 cannot be empty ")
        return None

    if len(coeffecients2) == 0:
        print("coeffecients2 cannot be empty ")
        return None

    denumerator=0
    for char in coeffecients2:
        denumerator+=int(char)*num

    if denumerator == 0:
        print("result is undefined")
        return None
        
    exponents1 = []
    for exponent1 in range(len(coeffecients1)-1,-1,-1):
        exponents1.append(exponent1)

    exponents2 = []
    for exponent2 in range(len(coeffecients2)-1,-1,-1):
        exponents2.append(exponent2)
        
    polynomial1=0
    polynomial2=0
	
    for i in range(len(coeffecients1)):
        polynomial1+=coeffecients1[i]*num**exponents1[i]
            
    for j in range(len(coeffecients2)):
        polynomial2+=coeffecients2[j]*num**exponents2[j]
            
    result=polynomial1/polynomial2
	
    return result

def get_exponential_value(num=1,constants=[1,2,3,4,5]):

    
    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if not isinstance(num,(int,float)):
        print("num must be a number")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None

    if len(constants) != 5:
        print("constants must not be empty ")
        return None
    
    # constants
    a=constants[0]
    b=constants[1]
    k=constants[2]
    h=constants[3]
    c=constants[4]
    
    result = (a*(b)**(k*(num+h)))+c

    return result

def get_sin_value(num=1,constants=[1,2,3,4]):

    
    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if not isinstance(num,(int,float)):
        print("num must be a number")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None

    if len(constants) != 4:
        print("constants must not be empty ")
        return None
    
    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]
    
    result = a*(math.sin(k*(num+h)))+c

    return result

def get_cos_value(num=1,constants=[1,2,3,4]):

    
    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if not isinstance(num,(int,float)):
        print("num must be a number")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None

    if len(constants) != 4:
        print("constants must not be empty ")
        return None
    
    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]
    
    result = a*(math.cos(k*(num+h)))+c

    return result

def get_deravitive_of_polynomial(num=1,coeffecients=[1,2,3]):

    if type(coeffecients) is not list:
        print("coeffecients must be of type array")
        return None

    if not isinstance(num,(int,float)):
        print("num must be a number")
        return None
    
    for char in coeffecients:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None

    if len(coeffecients) == 0:
        print("coeffecients must not be empty ")
        return None
		
		
    exponents = []
    for exponent in range(len(coeffecients)-1,-1,-1):
        exponents.append(exponent)
			
    diffcoeffecients = []
    diffexponents = []
    
    for i in range(len(coeffecients)):
        diffcoeffecients.append(coeffecients[i]*exponents[i])
        diffexponents.append(exponents[i]-1)
			
	
    deravitive = 0
		
    for j in range(len(coeffecients)):
        deravitive+=diffcoeffecients[j]*num**diffexponents[j]
				
    return deravitive

def get_secant_of_polynomial(coeffecients=[1,2,3],bounds=[0,1]):

    if type(coeffecients) is not list:
        print("coeffecients must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in coeffecients:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    exponents = []
    for exponent in range(len(coeffecients)-1,-1,-1):
        exponents.append(exponent)

    bounds.sort()
    
    output1=0
    output2=0
		
    for j in range(len(coeffecients)):
        output1+=coeffecients[j]*bounds[0]**exponents[j]
        output2+=coeffecients[j]*bounds[1]**exponents[j]
			
    if bounds[1]-bounds[0] == 0:
        print("result is undefined")
        return None
    
    slope = (output2-output1)/(bounds[1]-bounds[0])

    return slope

def get_secant_of_rational(coeffecients1=[1,2,3],coeffecients2=[1,2,3],bounds=[0,1]):

    if type(coeffecients1) is not list:
        print("coeffecients1 must be of type array")
        return None

    if type(coeffecients2) is not list:
        print("coeffecients2 must be of type array")
        return None
    
    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char1 in coeffecients1:
        if not isinstance(char1,(int,float)):
            print("all elements of constants1 must be numbers")
            return None
        
    for char2 in coeffecients2:
        if not isinstance(char2,(int,float)):
            print("all elements of constants2 must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
			
    exponents1=[]
    exponents2=[]
		
    for exponent1 in range(len(coeffecients1)-1,-1,-1):
        exponents1.append(exponent1)
        
    for exponent2 in range(len(coeffecients2)-1,-1,-1):
        exponents2.append(exponent2)	
			
    polynomial1=0
    polynomial2=0

    bounds.sort()
    
    for j in range(len(coeffecients1)):
        polynomial1+=coeffecients1[j]*bounds[0]**exponents1[j]
        polynomial2+=coeffecients1[j]*bounds[1]**exponents1[j]

    	
    polynomial3=0
    polynomial4=0
    
    for k in range(len(coeffecients2)):
        polynomial3+=coeffecients2[k]*bounds[0]**exponents2[k]
        polynomial4+=coeffecients2[k]*bounds[1]**exponents2[k]

    if polynomial3 == 0 or polynomial4 == 0:
        print("result is undefined")
        return None
    
    rational1= polynomial1/polynomial3
    rational2 = polynomial2/polynomial4

    if bounds[1]-bounds[0] == 0:
        print("result is undefined")
        return None
    
    slope = (rational2-rational1)/(bounds[1]-bounds[0])

    return slope
		
def get_deravitive_of_exponential(num=1,constants=[1,2,3,4,5]):
        
    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if not isinstance(num,(int,float)):
        print("num must be a number")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None

    if len(constants) != 5:
        print("constants must not be empty ")
        return None

    # constants
    a=constants[0]
    b=constants[1]
    k=constants[2]
    h=constants[3]
    c=constants[4]
    
    deravitive = a*k*((b)**(k*(num+h)))*math.log(b)
    
    return deravitive

def get_secant_of_exponential(constants=[1,2,3,4,5],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 5:
        print("constants must have length 5 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    # constants
    a=constants[0]
    b=constants[1]
    k=constants[2]
    h=constants[3]
    c=constants[4]
    
    bounds.sort()

    output1 = (a*(b)**(k*(bounds[0]+h)))+c
    output2 = (a*(b)**(k*(bounds[1]+h)))+c

    if bounds[1]-bounds[0] == 0:
        print("result is undefined")
        return None
    
    slope = (output2-output1)/(bounds[1]-bounds[0])
		
	
    return slope

def get_deravitive_of_sin(num=1,constants=[1,2,3,4,5]):
        
    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if not isinstance(num,(int,float)):
        print("num must be a number")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None

    if len(constants) != 4:
        print("constants must not be empty ")
        return None

    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]
    
    deravitive = a*k*(math.cos(k*(num+h)))
    
    return deravitive

def get_secant_of_sin(constants=[1,2,3,4],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 4:
        print("constants must have length 4 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]

    bounds.sort()
    
    output1 = a*(math.sin(k*(bounds[0]+h)))+c
    output2 = a*(math.sin(k*(bounds[1]+h)))+c

    if bounds[1]-bounds[0] == 0:
        print("result is undefined")
        return None
    
    slope = (output2-output1)/(bounds[1]-bounds[0])

    return slope

def get_secant_of_cos(constants=[1,2,3,4],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 4:
        print("constants must have length 4 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]

    bounds.sort()
    
    output1 = a*(math.cos(k*(bounds[0]+h)))+c
    output2 = a*(math.cos(k*(bounds[1]+h)))+c

    if bounds[1]-bounds[0] == 0:
        print("result is undefined")
        return None
    
    slope = (output2-output1)/(bounds[1]-bounds[0])

    return slope

def get_deravitive_of_cos(num=1,constants=[1,2,3,4,5]):
        
    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if not isinstance(num,(int,float)):
        print("num must be a number")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None

    if len(constants) != 4:
        print("constants must not be empty ")
        return None

    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]
    
    deravitive = -1*a*k*(math.sin(k*(num+h)));
    
    return deravitive


def get_exponential_integral(constants=[1,2,3,4,5],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 5:
        print("constants must have length 5 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    
    # constants
    a=constants[0]
    b=constants[1]
    k=constants[2]
    h=constants[3]
    c=constants[4]
    
    upper_integral=(a*(b)**(k*(bounds[1]+h)))/(math.log(b)*k)+c*bounds[1]
    lower_integral=(a*(b)**(k*(bounds[0]+h)))/(math.log(b)*k)+c*bounds[0]
    integral = upper_integral - lower_integral
		
    return integral

def get_sin_integral(constants=[1,2,3,4],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 4:
        print("constants must have length 5 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    
    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]
    
    upper_integral = -1*a*k*(math.cos(k*(bounds[1]+h)))+c*bounds[1]
    lower_integral = -1*a*k*(math.cos(k*(bounds[0]+h)))+c*bounds[0]
    integral = upper_integral - lower_integral
		
    return integral

def get_cos_integral(constants=[1,2,3,4],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 4:
        print("constants must have length 5 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    
    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]
    
    upper_integral = a*k*(math.sin(k*(bounds[1]+h)))+c*bounds[1]
    lower_integral = a*k*(math.sin(k*(bounds[0]+h)))+c*bounds[0]
    integral = upper_integral - lower_integral
		
    return integral

def get_exponential_average(constants=[1,2,3,4,5],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 5:
        print("constants must have length 5 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    
    # constants
    a=constants[0]
    b=constants[1]
    k=constants[2]
    h=constants[3]
    c=constants[4]
    
    upper_integral=(a*(b)**(k*(bounds[1]+h)))/(math.log(b)*k)+c*bounds[1]
    lower_integral=(a*(b)**(k*(bounds[0]+h)))/(math.log(b)*k)+c*bounds[0]
    integral = upper_integral - lower_integral
		
    return integral/(bounds[1]-bounds[0])

def get_sin_average(constants=[1,2,3,4],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 4:
        print("constants must have length 5 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    
    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]
    
    upper_integral = -1*a*k*(math.cos(k*(bounds[1]+h)))+c*bounds[1]
    lower_integral = -1*a*k*(math.cos(k*(bounds[0]+h)))+c*bounds[0]
    integral = upper_integral - lower_integral
		
    return integral/(bounds[1]-bounds[0])

def get_cos_average(constants=[1,2,3,4],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 4:
        print("constants must have length 4 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    
    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]
    
    upper_integral = a*k*(math.sin(k*(bounds[1]+h)))+c*bounds[1]
    lower_integral = a*k*(math.sin(k*(bounds[0]+h)))+c*bounds[0]
    integral = upper_integral - lower_integral
		
    return integral/(bounds[1]-bounds[0])

def get_exponential_area(constants1=[1,2,3,4,5],constants2=[1,2,3,4,5], bounds=[0,1]):

    if type(constants1) is not list:
        print("constants1 must be of type array")
        return None

    if type(constants2) is not list:
        print("constants1 must be of type array")
        return None
    
    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char1 in constants1:
        if not isinstance(char1,(int,float)):
            print("all elements of constants1 must be numbers")
            return None
        
    for char2 in constants2:
        if not isinstance(char2,(int,float)):
            print("all elements of constants2 must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants1) != 5:
        print("constants1 must have length 5 ")
        return None

    if len(constants2) != 5:
        print("constants2 must have length 5 ")
        return None
    
    if len(bounds) != 2:
        print("bounds must have length 2")
        return None

    a1= constants1[0]
    b1=constants1[1]
    k1= constants1[2]
    h1= constants1[3]
    c1=constants1[4]

    a2= constants2[0]
    b2=constants2[1]
    k2= constants2[2]
    h2= constants2[3]
    c2=constants2[4]
    
    upper_integral1=(a1*(b1)**(k1*(bounds[1]+h1)))/(math.log(b1)*k1)+c1*bounds[1]
    upper_integral2=(a2*(b2)**(k2*(bounds[1]+h2)))/(math.log(b2)*k2)+c2*bounds[1]
    lower_integral1=(a1*(b1)**(k1*(bounds[0]+h1)))/(math.log(b1)*k1)+c1*bounds[0]
    lower_integral2=(a2*(b2)**(k2*(bounds[0]+h2)))/(math.log(b2)*k2)+c2*bounds[0]
    integral1 = upper_integral1 - lower_integral1
    integral2 = upper_integral2 - lower_integral2
    area = abs(integral2 - integral1)
		
    return area

def get_sin_area(constants1=[1,2,3,4],constants2=[1,2,3,4], bounds=[0,1]):

    if type(constants1) is not list:
        print("constants1 must be of type array")
        return None

    if type(constants2) is not list:
        print("constants1 must be of type array")
        return None
    
    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char1 in constants1:
        if not isinstance(char1,(int,float)):
            print("all elements of constants1 must be numbers")
            return None
        
    for char2 in constants2:
        if not isinstance(char2,(int,float)):
            print("all elements of constants2 must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants1) != 4:
        print("constants1 must have length 5 ")
        return None

    if len(constants2) != 4:
        print("constants2 must have length 5 ")
        return None
    
    if len(bounds) != 2:
        print("bounds must have length 2")
        return None

    bounds.sort()
    
    a1= constants1[0]
    k1= constants1[1]
    h1= constants1[2]
    c1=constants1[3]

    a2= constants2[0]
    k2= constants2[1]
    h2= constants2[2]
    c2=constants2[3]
    
    upper_integral1 = -1*a1*k1*(math.cos(k1*(bounds[1]+h1)))+c1*bounds[1]
    upper_integral2 = -1*a2*k2*(math.cos(k2*(bounds[1]+h2)))+c2*bounds[1]
    lower_integral1 = -1*a1*k1*(math.cos(k1*(bounds[0]+h1)))+c1*bounds[0]
    lower_integral2 = -1*a2*k2*(math.cos(k2*(bounds[0]+h2)))+c2*bounds[0]
    integral1 = upper_integral1 - lower_integral1
    integral2 = upper_integral2 - lower_integral2
    area = abs(integral2 - integral1)
		
    return area

def get_cos_area(constants1=[1,2,3,4],constants2=[1,2,3,4], bounds=[0,1]):

    if type(constants1) is not list:
        print("constants1 must be of type array")
        return None

    if type(constants2) is not list:
        print("constants1 must be of type array")
        return None
    
    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char1 in constants1:
        if not isinstance(char1,(int,float)):
            print("all elements of constants1 must be numbers")
            return None
        
    for char2 in constants2:
        if not isinstance(char2,(int,float)):
            print("all elements of constants2 must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants1) != 4:
        print("constants1 must have length 5 ")
        return None

    if len(constants2) != 4:
        print("constants2 must have length 5 ")
        return None
    
    if len(bounds) != 2:
        print("bounds must have length 2")
        return None

    bounds.sort()
    
    a1= constants1[0]
    k1= constants1[1]
    h1= constants1[2]
    c1=constants1[3]

    a2= constants2[0]
    k2= constants2[1]
    h2= constants2[2]
    c2=constants2[3]
    
    upper_integral1 = a1*k1*(math.sin(k1*(bounds[1]+h1)))+c1*bounds[1]
    upper_integral2 = a2*k2*(math.sin(k2*(bounds[1]+h2)))+c2*bounds[1]
    lower_integral1 = a1*k1*(math.sin(k1*(bounds[0]+h1)))+c1*bounds[0]
    lower_integral2 = a2*k2*(math.sin(k2*(bounds[0]+h2)))+c2*bounds[0]
    integral1 = upper_integral1 - lower_integral1
    integral2 = upper_integral2 - lower_integral2
    area = abs(integral2 - integral1)
		
    return area

def get_sin_max(constants=[1,2,3,4],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 4:
        print("constants must have length 4 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    x=bounds[0]
    
    critical_values=[bounds[0],bounds[1]]
    deravitive=0

    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]

    
    while x<=bounds[1]:
    
        deravitive=0
        deravitive = a*k*(math.cos(k*(x+h)))
        if (-0.0005<=deravitive<=0.0005):
            critical_values.append(x);
					
        x+=0.001	    
    
    outputs=[]	
	
    for i in range(len(critical_values)):
        output=0
        output = a*k*(math.cos(k*(critical_values[i]+h)))
        outputs.append(output)	
			
		
    maximum = outputs[0]
    for j in range(len(outputs)):
        if outputs[j] >= maximum:
            maximum = outputs[j]
				
    return maximum

def get_exponential_max(constants=[1,2,3,4,5],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 5:
        print("constants must have length 5 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    x=bounds[0]
    
    critical_values=[bounds[0],bounds[1]]
    deravitive=0

    # constants
    a=constants[0]
    b=constants[1]
    k=constants[2]
    h=constants[3]
    c=constants[4]

    
    while x<=bounds[1]:
    
        deravitive=0
        deravitive = a*k*((b)**(k*(x+h)))*math.log(b)
        if (-0.0005<=deravitive<=0.0005):
            critical_values.append(x);
					
        x+=0.001	    
    
    outputs=[]	
	
    for i in range(len(critical_values)):
        output=0
        output = (a*(b)**(k*(critical_values[i]+h)))+c
        outputs.append(output)	
			
		
    maximum = outputs[0]
    for j in range(len(outputs)):
        if outputs[j] >= maximum:
            maximum = outputs[j]
				
    return maximum

def get_sin_min(constants=[1,2,3,4],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 4:
        print("constants must have length 4 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    x=bounds[0]
    
    critical_values=[bounds[0],bounds[1]]
    deravitive=0

    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]

    
    while x<=bounds[1]:
    
        deravitive=0
        deravitive = a*k*(math.cos(k*(x+h)))
        if (-0.0005<=deravitive<=0.0005):
            critical_values.append(x);
					
        x+=0.001	    
    
    outputs=[]	
	
    for i in range(len(critical_values)):
        output=0
        output = a*k*(math.sin(k*(critical_values[i]+h)))
        outputs.append(output)	
			
		
    minimum = outputs[0]
    for j in range(len(outputs)):
        if outputs[j] <= minimum:
            minimum = outputs[j]
				
    return minimum

def get_cos_max(constants=[1,2,3,4],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 4:
        print("constants must have length 4 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    x=bounds[0]
    
    critical_values=[bounds[0],bounds[1]]
    deravitive=0

    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]

    
    while x<=bounds[1]:
    
        deravitive=0
        deravitive = -1*a*k*(math.sin(k*(x+h)))
        if (-0.0005<=deravitive<=0.0005):
            critical_values.append(x);
					
        x+=0.001	    
    
    outputs=[]	
	
    for i in range(len(critical_values)):
        output=0
        output = a*k*(math.cos(k*(critical_values[i]+h)))
        outputs.append(output)	
			
		
    maximum = outputs[0]
    for j in range(len(outputs)):
        if outputs[j] >= maximum:
            maximum = outputs[j]
				
    return maximum

def get_cos_min(constants=[1,2,3,4],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 4:
        print("constants must have length 4 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    x=bounds[0]
    
    critical_values=[bounds[0],bounds[1]]
    deravitive=0

    # constants
    a=constants[0]
    k=constants[1]
    h=constants[2]
    c=constants[3]

    
    while x<=bounds[1]:
    
        deravitive=0
        deravitive = -1*a*k*(math.sin(k*(x+h)))
        if (-0.0005<=deravitive<=0.0005):
            critical_values.append(x);
					
        x+=0.001	    
    
    outputs=[]	
	
    for i in range(len(critical_values)):
        output=0
        output = a*k*(math.cos(k*(critical_values[i]+h)))
        outputs.append(output)	
			
		
    minimum = outputs[0]
    for j in range(len(outputs)):
        if outputs[j] <= minimum:
            minimum = outputs[j]
				
    return minimum

def get_exponential_min(constants=[1,2,3,4,5],bounds=[0,1]):

    if type(constants) is not list:
        print("constants must be of type array")
        return None

    if type(bounds) is not list:
        print("bounds must be of type array")
        return None
    
    for char in constants:
        if not isinstance(char,(int,float)):
            print("all elements of constants must be numbers")
            return None
        
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
    
    if len(constants) != 5:
        print("constants must have length 5 ")
        return None

    if len(bounds) != 2:
        print("bounds must have length 2")
        return None
    
    bounds.sort()
    x=bounds[0]
    
    critical_values=[bounds[0],bounds[1]]
    deravitive=0

    # constants
    a=constants[0]
    b=constants[1]
    k=constants[2]
    h=constants[3]
    c=constants[4]

    
    while x<=bounds[1]:
    
        deravitive=0
        deravitive = a*k*((b)**(k*(x+h)))*math.log(b)
        if -0.0005<=deravitive<=0.0005:
            critical_values.append(x)
					
        x+=0.001		
    
    outputs=[]	
	
    for i in range(len(critical_values)):
        output=0
        output = (a*(b)**(k*(critical_values[i]+h)))+c
        outputs.append(output)	
			
		
    minimum = outputs[0]
    for j in range(len(outputs)):
        if outputs[j] <= minimum:
            minimum = outputs[j]
				
    return minimum
   
def get_deravitive_of_rational(num=1,coeffecients1=[1],coeffecients2=[1]):

    if type(coeffecients1) is not list:
        print("coeffecient1 must be of type array ")
        return None
        
    if type(coeffecients2) is not list:
        print("coeffecient2 must be of type array ")
        return None
        
    for char in coeffecients1:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecient1 must be numbers")
            return None

    for char in coeffecients2:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecient2 must be numbers")
            return None
            
    if len(coeffecients1) == 0:
        print("coeffecients1 cannot be empty ")
        return None

    if len(coeffecients2) == 0:
        print("coeffecients2 cannot be empty ")
        return None
       
    exponents1 = []
    for exponent1 in range(len(coeffecients1)-1,-1,-1):
        exponents1.append(exponent1)

    exponents2 = []
    for exponent2 in range(len(coeffecients2)-1,-1,-1):
        exponents2.append(exponent2)
            	
		
    num1=num-0.000001
    num2=num+0.000001

    if (num2-num1)== 0:
        print("result is undefined")
        return None
        
    polynomial1=0
    polynomial2=0
		
    for i in range(len(coeffecients1)):
        polynomial1+=coeffecients1[i]*num1**exponents1[i]
        polynomial2+=coeffecients1[i]*num2**exponents1[i]

    polynomial3=0
    polynomial4=0
	
    for j in range(len(coeffecients2)):
        polynomial3+=coeffecients2[j]*num1**exponents2[j]
        polynomial4+=coeffecients2[j]*num2**exponents2[j]
			
	    
    rational1= polynomial1/polynomial3
    rational2 = polynomial2/polynomial4
    deravitive = (rational2-rational1)/(num2-num1)

    return deravitive


def get_polynomial_integral(coeffecients=[1],bounds=[0,1]):

    if type(coeffecients) is not list:
        print("coeffecient must be of type array ")
        return None
        
    if type(bounds) is not list:
        print("bounds must be of type array ")
        return None
        
    for char in coeffecients:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients must be numbers")
            return None

    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
            
    if len(coeffecients) == 0:
        print("coeffecients cannot be empty ")
        return None

    if len(bounds) !=2:
        print("bounds must have length 2 ")
        return None

    bounds.sort()
        
    exponents = []
    for exponent in range(len(coeffecients)-1,-1,-1):
        exponents.append(exponent)
		
    anticoeffecients=[]
    antiexponents=[]
	
    for i in range(len(coeffecients)):
        anticoeffecients.append((coeffecients[i]/(exponents[i]+1)))
        antiexponents.append(exponents[i]+1)
			
	
    lower_integral=0
    upper_integral=0
		
    for j in range(len(coeffecients)):
        lower_integral+=anticoeffecients[j]*bounds[0]**antiexponents[j];
        upper_integral+=anticoeffecients[j]*bounds[1]**antiexponents[j];

    return upper_integral-lower_integral
    
def get_polynomial_area(coeffecients1=[1],coeffecients2=[1],bounds=[0,1]):

    if type(coeffecients1) is not list:
        print("coeffecients1 must be of type array ")
        return None

    if type(coeffecients2) is not list:
        print("coeffecient2s must be of type array ")
        return None
        
        if type(bounds) is not list:
            print("bounds must be of type array ")
            return None
        
    for char in coeffecients1:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients1 must be numbers")
            return None

    for char in coeffecients2:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients2 must be numbers")
            return None
            
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
            
    if len(coeffecients1) == 0:
        print("coeffecients1 cannot be empty ")
        return None

    if len(coeffecients2) == 0:
        print("coeffecients2 cannot be empty ")
        return None
        
    if len(bounds) !=2:
        print("bounds must have length 2 ")
        return None
        
    exponents1 = []
    exponents2 = []
	
    for exponent1 in range(len(coeffecients1)-1,-1,-1):
        exponents1.append(exponent1)
			
    for exponent2 in range(len(coeffecients2)-1,-1,-1):
        exponents2.append(exponent2)
	    
    anticoeffecients1 = []
    anticoeffecients2 = []
    antiexponents1 = []
    antiexponents2 = []
		
    for i in range(len(coeffecients1)):
        anticoeffecients1.append((coeffecients1[i]/(exponents1[i]+1)))
        antiexponents1.append(exponents1[i]+1)
			
			
    for j in range(len(coeffecients2)):
        anticoeffecients2.append((coeffecients2[j]/(exponents2[j]+1)))
        antiexponents2.append(exponents2[j]+1)
		    
    bounds.sort()
	
    lower_integral1=0
    upper_integral1=0
    lower_integral2=0
    upper_integral2=0
		
    for i in range(len(coeffecients1)):
        lower_integral1+=anticoeffecients1[i]*bounds[0]**antiexponents1[i]
        upper_integral1+=anticoeffecients1[i]*bounds[1]**antiexponents1[i]
			
    for j in range(len(coeffecients2)):
        lower_integral2+=anticoeffecients2[j]*bounds[0]**antiexponents2[j]
        upper_integral2+=anticoeffecients2[j]*bounds[1]**antiexponents2[j]
			
    				
    integral1 = upper_integral1 - lower_integral1
    integral2 = upper_integral2 - lower_integral2
    area = abs(integral2-integral1)
		
    return area
    
def get_rational_integral(coeffecients1=[1],coeffecients2=[1],bounds=[0.1]):

        if type(coeffecients1) is not list:
            print("coeffecient1 must be of type array ")
            return None

        if type(coeffecients2) is not list:
            print("coeffecient2 must be of type array ")
            return None
        
        if type(bounds) is not list:
            print("bounds must be of type array ")
            return None
        
        for char in coeffecients1:
            if not isinstance(char,(int,float)):
                print("all elements of coeffecients1 must be numbers")
                return None

        for char in coeffecients2:
            if not isinstance(char,(int,float)):
                print("all elements of coeffecients2 must be numbers")
                return None
            
        for char in bounds:
            if not isinstance(char,(int,float)):
                print("all elements of bounds must be numbers")
                return None
            
        if len(coeffecients1) == 0:
            print("coeffecients1 cannot be empty ")
            return None

        if len(coeffecients2) == 0:
            print("coeffecients2 cannot be empty ")
            return None
        
        if len(bounds) !=2:
            print("bounds must have length 2 ")
            return None
        
        exponents1 = []
        exponents2 = []
	
        for exponent1 in range(len(coeffecients1)-1,-1,-1):
            exponents1.append(exponent1)
			
        for exponent2 in range(len(coeffecients2)-1,-1,-1):
            exponents2.append(exponent2)
			
        rational=0
        integral=0
        polynomial1=0
        polynomial2=0

        bounds.sort()
        x= bounds[0]
	
        while x<=bounds[1]:
    
            for i in range(len(coeffecients1)):
                polynomial1+=coeffecients1[i]*x**exponents1[i]
			
		    
            for j in range(len(coeffecients2)):
                polynomial2+=coeffecients2[j]*x**exponents2[j]

            if polynomial2 != 0:
                rational=polynomial1/polynomial2
                integral+=0.001*rational
                
            polynomial1=0
            polynomial2=0
            rational=0
            
            x+=0.001

        return integral

def get_rational_average(coeffecients1=[1],coeffecients2=[1],bounds=[0.1]):

        if type(coeffecients1) is not list:
            print("coeffecient1 must be of type array ")
            return None

        if type(coeffecients2) is not list:
            print("coeffecient2 must be of type array ")
            return None
        
        if type(bounds) is not list:
            print("bounds must be of type array ")
            return None
        
        for char in coeffecients1:
            if not isinstance(char,(int,float)):
                print("all elements of coeffecients1 must be numbers")
                return None

        for char in coeffecients2:
            if not isinstance(char,(int,float)):
                print("all elements of coeffecients2 must be numbers")
                return None
            
        for char in bounds:
            if not isinstance(char,(int,float)):
                print("all elements of bounds must be numbers")
                return None
            
        if len(coeffecients1) == 0:
            print("coeffecients1 cannot be empty ")
            return None

        if len(coeffecients2) == 0:
            print("coeffecients2 cannot be empty ")
            return None
        
        if len(bounds) !=2:
            print("bounds must have length 2 ")
            return None
        
        exponents1 = []
        exponents2 = []
	
        for exponent1 in range(len(coeffecients1)-1,-1,-1):
            exponents1.append(exponent1)
			
        for exponent2 in range(len(coeffecients2)-1,-1,-1):
            exponents2.append(exponent2)
			
        rational=0
        integral=0
        polynomial1=0
        polynomial2=0

        bounds.sort()
        x= bounds[0]
	
        while x<=bounds[1]:
    
            for i in range(len(coeffecients1)):
                polynomial1+=coeffecients1[i]*x**exponents1[i]
			
		    
            for j in range(len(coeffecients2)):
                polynomial2+=coeffecients2[j]*x**exponents2[j]
	    
			
            if polynomial2 != 0:
                rational=polynomial1/polynomial2
                integral+=0.001*rational
                
            polynomial1=0
            polynomial2=0
            rational=0
            
            x+=0.001

        return integral/(bounds[1]-bounds[0])
    
def get_rational_area(coeffecients1=[1],coeffecients2=[1],coeffecients3=[1],coeffecients4=[1],bounds=[0,1]):

    if type(coeffecients1) is not list:
        print("coeffecient1 must be of type array ")
        return None

    if type(coeffecients2) is not list:
        print("coeffecient2 must be of type array ")
        return None

    if type(coeffecients3) is not list:
        print("coeffecient3 must be of type array ")
        return None

    if type(coeffecients4) is not list:
        print("coeffecient4 must be of type array ")
        return None
        
    if type(bounds) is not list:
        print("bounds must be of type array ")
        return None
        
    for char in coeffecients1:
        if not isinstance(char,(int,float)):
             print("all elements of coeffecients1 must be numbers")
             return None
        
    for char in coeffecients2:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients2 must be numbers")
            return None

    for char in coeffecients3:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients3 must be numbers")
            return None

    for char in coeffecients4:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients4 must be numbers")
            return None
            
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
            
    if len(coeffecients1) == 0:
        print("coeffecients1 cannot be empty ")
        return None

    if len(coeffecients2) == 0:
        print("coeffecients2 cannot be empty ")
        return None

    if len(coeffecients3) == 0:
        print("coeffecients3 cannot be empty ")
        return None

    if len(coeffecients4) == 0:
        print("coeffecients4 cannot be empty ")
        return None
        
    if len(bounds) !=2:
        print("bounds must have length 2 ")
        return None
        
    exponents1 = []
    exponents2 = []
    exponents3 = []
    exponents4 = []
		
    for exponent1 in range(len(coeffecients1)):
        exponents1.append(exponent1)

    for exponent2 in range(len(coeffecients2)):
        exponents2.append(exponent2)	

    for exponent3 in range(len(coeffecients3)):
        exponents3.append(exponent3)
            
    for exponent4 in range(len(coeffecients4)):
        exponents4.append(exponent4)
		
    bounds.sort()
    x= bounds[0]
	
    rational1=0
    rational2=0
    area=0
    polynomial1=0
    polynomial2=0
    polynomial3=0
    polynomial4=0
	
    while x<=bounds[1]:
            
        for i in range(len(coeffecients1)):
            polynomial1+=coeffecients1[i]*x**exponents1[i]

        for j in range(len(coeffecients2)):
            polynomial2+=coeffecients2[j]*x**exponents2[j]

        for k in range(len(coeffecients3)):
            polynomial3+=coeffecients3[k]*x**exponents3[k]	

        for l in range(len(coeffecients4)):
            polynomial4+=coeffecients4[l]*x**exponents4[l]
		
        if polynomial2 != 0:
            rational1=polynomial1/polynomial2
        
        if polynomial4 !=0:
            rational2=polynomial3/polynomial4
            
        if polynomial2 !=0 and polynomial4 !=0:
            area+=0.001*abs(rational2-rational1)
			
        polynomial1=0
        polynomial2=0
        polynomial3=0
        polynomial4=0
        rational1=0
        rational2=0
		
        x+=0.001

    return area

def get_polynomial_average(coeffecients=[1],bounds=[0,1]):

    if type(coeffecients) is not list:
        print("coeffecient must be of type array ")
        return None
        
    if type(bounds) is not list:
        print("bounds must be of type array ")
        return None
        
    for char in coeffecients:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients must be numbers")
            return None

    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
            
    if len(coeffecients) == 0:
        print("coeffecients cannot be empty ")
        return None

    if len(bounds) !=2:
        print("bounds must have length 2 ")
        return None

    bounds.sort()
        
    exponents = []
    for exponent in range(len(coeffecients)-1,-1,-1):
        exponents.append(exponent)
		
    anticoeffecients=[]
    antiexponents=[]
	
    for i in range(len(coeffecients)):
        anticoeffecients.append((coeffecients[i]/(exponents[i]+1)))
        antiexponents.append(exponents[i]+1)
			
	
    lower_integral=0
    upper_integral=0
		
    for j in range(len(coeffecients)):
        lower_integral+=anticoeffecients[j]*bounds[0]**antiexponents[j];
        upper_integral+=anticoeffecients[j]*bounds[1]**antiexponents[j];

    return (upper_integral-lower_integral)/(bounds[1]-bounds[0])

def get_polynomial_max(coeffecients=[1],bounds=[0,1]):

    if type(coeffecients) is not list:
        print("coeffecient must be of type array ")
        return None
        
    if type(bounds) is not list:
        print("bounds must be of type array ")
        return None
        
    for char in coeffecients:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients must be numbers")
            return None

    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
            
    if len(coeffecients) == 0:
        print("coeffecients cannot be empty ")
        return None

    if len(bounds) !=2:
        print("bounds must have length 2 ")
        return None
		
    bounds.sort()

    exponents = []
    for exponent in range(len(coeffecients)-1,-1,-1):
        exponents.append(exponent)
        
    diffcoeffecients = []
    diffexponents = []
    
    for i in range(len(coeffecients)):
        diffcoeffecients.append(coeffecients[i]*exponents[i])
        diffexponents.append(exponents[i]-1)
			
			
    critical_values=[bounds[0],bounds[1]]
    x = bounds[0]

    while x<=bounds[1]:
        
        deravitive=0
        
        for j in range(len(coeffecients)):
            deravitive+=diffcoeffecients[j]*x**diffexponents[j]
				
            if -0.0005<=deravitive<=0.0005:
                critical_values.append(x)
                
        x+=0.001			
		
    outputs= []
    
    for k in range(len(critical_values)):
        output=0
        for l in range(len(coeffecients)):
            output+=coeffecients[l]*critical_values[k]**exponents[l]
				
        outputs.append(output)
			
		
    maximum = outputs[0]
    for m in range(len(outputs)):
        if outputs[m] >= maximum:
            maximum = outputs[m]
					
    return maximum

def get_polynomial_min(coeffecients=[1],bounds=[0,1]):

    if type(coeffecients) is not list:
        print("coeffecient must be of type array ")
        return None
        
    if type(bounds) is not list:
        print("bounds must be of type array ")
        return None
        
    for char in coeffecients:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients must be numbers")
            return None

    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
            
    if len(coeffecients) == 0:
        print("coeffecients cannot be empty ")
        return None

    if len(bounds) !=2:
        print("bounds must have length 2 ")
        return None
		
    bounds.sort()

    exponents = []
    for exponent in range(len(coeffecients)-1,-1,-1):
        exponents.append(exponent)
        
    diffcoeffecients = []
    diffexponents = []
    
    for i in range(len(coeffecients)):
        diffcoeffecients.append(coeffecients[i]*exponents[i])
        diffexponents.append(exponents[i]-1)
			
			
    critical_values=[bounds[0],bounds[1]]
    x = bounds[0]

    while x<=bounds[1]:
        
        deravitive=0
        
        for j in range(len(coeffecients)):
            deravitive+=diffcoeffecients[j]*x**diffexponents[j]
				
            if -0.0005<=deravitive<=0.0005:
                critical_values.append(x)
                
        x+=0.001			
		
    outputs= []
    
    for k in range(len(critical_values)):
        output=0
        for l in range(len(coeffecients)):
            output+=coeffecients[l]*critical_values[k]**exponents[l]
				
        outputs.append(output)
			
		
    minimum = outputs[0]
    for m in range(len(outputs)):
        if outputs[m] <= minimum:
            minimum = outputs[m]
					
    return minimum

def get_rational_max(coeffecients1=[1],coeffecients2=[1],bounds=[0,1]):

    if type(coeffecients1) is not list:
        print("coeffecient1 must be of type array ")
        return None

    if type(coeffecients2) is not list:
        print("coeffecient2 must be of type array ")
        return None
        
    if type(bounds) is not list:
        print("bounds must be of type array ")
        return None
        
    for char in coeffecients1:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients1 must be numbers")
            return None

    for char in coeffecients2:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients2 must be numbers")
            return None
            
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
            
    if len(coeffecients1) == 0:
        print("coeffecients1 cannot be empty ")
        return None

    if len(coeffecients2) == 0:
        print("coeffecients2 cannot be empty ")
        return None
        
    if len(bounds) !=2:
        print("bounds must have length 2 ")
        return None
        
   
			
    exponents1 = []
    exponents2 = []
		
		
    for exponent1 in range(len(coeffecients1)-1,-1,-1):
        exponents1.append(exponent1)
		
    for exponent2 in range(len(coeffecients2)-1,-1,-1):
        exponents2.append(exponent2)
            
    diffcoeffecients1 = []
    diffexponents1 = []
    diffcoeffecients2 = []
    diffexponents2 = []
		
    for i in range(len(coeffecients1)):
        diffcoeffecients1.append(coeffecients1[i]*exponents1[i])
        diffexponents1.append(exponents1[i]-1);
			
		
    for j in range(len(coeffecients2)):
        diffcoeffecients2.append(coeffecients2[j]*exponents2[j]);
        diffexponents2.append(exponents2[j]-1)
			
    bounds.sort()
    x = bounds[0]
        
    critical_values =[]
    outputs = []
    polynomial1=0
    polynomial2=0
    polynomial3=0
    polynomial4=0
    rational1=0
    rational2=0
    deravitive=0
	
	
    while x<=bounds[1]:
        for k in range(len(coeffecients1)):
            polynomial1+=coeffecients1[k]*(x-0.00001)**exponents1[k]
            polynomial2+=coeffecients1[k]*(x+0.00001)**exponents1[k]

        for l in range(len(coeffecients2)):
            polynomial3+=coeffecients2[l]*(x-0.00001)**exponents2[l]
            polynomial4+=coeffecients2[l]*(x+0.00001)**exponents2[l]

        if polynomial2 == 0 or polynomial4 == 0:
            print("result is undefined")
            return None
            
        rational1=polynomial1/polynomial3
        rational2=polynomial2/polynomial4
        deravitive = (rational2-rational1)/(0.00002)
	    
        if -0.0005<=deravitive<=0.0005 or abs(bounds[0]-x)<=0.05 or abs(bounds[1]-x)<=0.05:
            critical_values.append(x)
            outputs.append((rational1+rational2)/2)
				
        x+=0.001
	    
    maximum= outputs[0]
    for m in range(len(outputs)):
        if outputs[m] >= maximum:
            maximum = outputs[m]
					
    return maximum

def get_rational_min(coeffecients1=[1],coeffecients2=[1],bounds=[0,1]):

    if type(coeffecients1) is not list:
        print("coeffecient1 must be of type array ")
        return None

    if type(coeffecients2) is not list:
        print("coeffecient2 must be of type array ")
        return None
        
    if type(bounds) is not list:
        print("bounds must be of type array ")
        return None
        
    for char in coeffecients1:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients1 must be numbers")
            return None

    for char in coeffecients2:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients2 must be numbers")
            return None
            
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
            
    if len(coeffecients1) == 0:
        print("coeffecients1 cannot be empty ")
        return None

    if len(coeffecients2) == 0:
        print("coeffecients2 cannot be empty ")
        return None
        
    if len(bounds) !=2:
        print("bounds must have length 2 ")
        return None
        

			
    exponents1 = []
    exponents2 = []
		
		
    for exponent1 in range(len(coeffecients1)-1,-1,-1):
        exponents1.append(exponent1)
		
    for exponent2 in range(len(coeffecients2)-1,-1,-1):
        exponents2.append(exponent2)
            
    diffcoeffecients1 = []
    diffexponents1 = []
    diffcoeffecients2 = []
    diffexponents2 = []
		
    for i in range(len(coeffecients1)):
        diffcoeffecients1.append(coeffecients1[i]*exponents1[i])
        diffexponents1.append(exponents1[i]-1);
			
		
    for j in range(len(coeffecients2)):
        diffcoeffecients2.append(coeffecients2[j]*exponents2[j]);
        diffexponents2.append(exponents2[j]-1)
			
    bounds.sort()
    x = bounds[0]
        
    critical_values =[]
    outputs = []
    polynomial1=0
    polynomial2=0
    polynomial3=0
    polynomial4=0
    rational1=0
    rational2=0
    deravitive=0
	
	
    while x<=bounds[1]:
        for k in range(len(coeffecients1)):
            polynomial1+=coeffecients1[k]*(x-0.00001)**exponents1[k]
            polynomial2+=coeffecients1[k]*(x+0.00001)**exponents1[k]
				

        for l in range(len(coeffecients2)):
            polynomial3+=coeffecients2[l]*(x-0.00001)**exponents2[l]
            polynomial4+=coeffecients2[l]*(x+0.00001)**exponents2[l]

        if polynomial2 == 0 or polynomial4 == 0:
            print("result is undefined")
            return None
        
        rational1=polynomial1/polynomial3
        rational2=polynomial2/polynomial4
        deravitive = (rational2-rational1)/(0.00002)
	    
        if -0.0005<=deravitive<=0.0005 or abs(bounds[0]-x)<=0.05 or abs(bounds[1]-x)<=0.05:
            critical_values.append(x)
            outputs.append((rational1+rational2)/2)

        x+=0.001
	
    minimum= outputs[0]
    for m in range(len(outputs)):
        if outputs[m] <= minimum:
            minimum = outputs[m]
					
    return minimum

def solve_polynomial(coeffecients1=[1], coeffecients2=[1], bounds=[0,1]):

    if type(coeffecients1) is not list:
        print("coeffecient1 must be of type array ")
        return None

    if type(coeffecients2) is not list:
        print("coeffecient2 must be of type array ")
        return None
        
    if type(bounds) is not list:
        print("bounds must be of type array ")
        return None
        
    for char in coeffecients1:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients1 must be numbers")
            return None

    for char in coeffecients2:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients2 must be numbers")
            return None
            
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
            
    if len(coeffecients1) == 0:
        print("coeffecients1 cannot be empty ")
        return None

    if len(coeffecients2) == 0:
        print("coeffecients2 cannot be empty ")
        return None
        
    if len(bounds) !=2:
        print("bounds must have length 2 ")
        return None
		
    exponents1=[]
    exponents2=[]
		
		
    for exponent1 in range(len(coeffecients1)-1,-1,-1):
        exponents1.append(exponent1)
		
    for exponent2 in range(len(coeffecients2)-1,-1,-1):
        exponents2.append(exponent2)

    bounds.sort()
    x=bounds[0]
    
    polynomial1=0
    polynomial2=0
		
    solutions=[]

    while x<=bounds[1]:
			
        for i in range(len(coeffecients1)):
            polynomial1+=coeffecients1[i]*x**exponents1[i]
			
				
				
        for j in range(len(coeffecients2)):
            polynomial2+=coeffecients2[j]*x**exponents2[j]
			
				
		    
        if abs(polynomial2-polynomial1)<0.05:
            solutions.append(x)
				
			
        polynomial1=0
        polynomial2=0

        x+=0.001
	
    return solutions
    
def solve_rational(coeffecients1=[1],coeffecients2=[1],coeffecients3=[1],coeffecients4=[1],bounds=[0,1]):

    if type(coeffecients1) is not list:
        print("coeffecient1 must be of type array ")
        return None

    if type(coeffecients2) is not list:
        print("coeffecient2 must be of type array ")
        return None

    if type(coeffecients3) is not list:
        print("coeffecient3 must be of type array ")
        return None

    if type(coeffecients4) is not list:
        print("coeffecient4 must be of type array ")
        return None
        
    if type(bounds) is not list:
        print("bounds must be of type array ")
        return None
        
    for char in coeffecients1:
        if not isinstance(char,(int,float)):
             print("all elements of coeffecients1 must be numbers")
             return None
        
    for char in coeffecients2:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients2 must be numbers")
            return None

    for char in coeffecients3:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients3 must be numbers")
            return None

    for char in coeffecients4:
        if not isinstance(char,(int,float)):
            print("all elements of coeffecients4 must be numbers")
            return None
            
    for char in bounds:
        if not isinstance(char,(int,float)):
            print("all elements of bounds must be numbers")
            return None
            
    if len(coeffecients1) == 0:
        print("coeffecients1 cannot be empty ")
        return None

    if len(coeffecients2) == 0:
        print("coeffecients2 cannot be empty ")
        return None

    if len(coeffecients3) == 0:
        print("coeffecients3 cannot be empty ")
        return None

    if len(coeffecients4) == 0:
        print("coeffecients4 cannot be empty ")
        return None
        
    if len(bounds) !=2:
        print("bounds must have length 2 ")
        return None

    exponents1=[]
    exponents2=[]
    exponents3=[]
    exponents4=[]
		
    for exponent1 in range(len(coeffecients1)-1,-1,-1):
        exponents1.append(exponent1)
		
    for exponent2 in range(len(coeffecients2)-1,-1,-1):
        exponents2.append(exponent2)

    for exponent3 in range(len(coeffecients3)-1,-1,-1):
        exponents3.append(exponent3)
		
    for exponent4 in range(len(coeffecients4)-1,-1,-1):
        exponents4.append(exponent4)

    bounds.sort()
    x=bounds[0]
    
    polynomial1=0
    polynomial2=0
    polynomial3=0
    polynomial4=0
    rational1=0
    rational2=0
		
    solutions=[]

    while x<=bounds[1]:
			
        for i in range(len(coeffecients1)):
            polynomial1+=coeffecients1[i]*x**exponents1[i]
		    
				
        for k in range(len(coeffecients2)):
            polynomial2+=coeffecients2[k]*x**exponents2[k]
			
				
        for l in range(len(coeffecients3)):
            polynomial3+=coeffecients3[l]*x**exponents3[l]
			
				
        for m in range(len(coeffecients4)):
            polynomial4+=coeffecients4[m]*x**exponents4[m]

        if polynomial2 == 0 or polynomial4 == 0:
            print("result is undefined")
            return None
	
        rational1=polynomial1/polynomial2;
        rational2=polynomial3/polynomial4;
				
        if abs(rational2-rational1)<0.05:
            solutions.append(x)
				
			
        rational1=0
        rational2=0
        polynomial1=0
        polynomial2=0
        polynomial3=0
        polynomial4=0
		
        x+=0.001
	
    return solutions  
    
