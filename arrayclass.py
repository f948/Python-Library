import helper_functions
import math

class Array:

    ''' This class creates instances of the array object'''
    
    # class attributes
    num_arrays = 0
    array_arrays=[]
    
    def __init__(self,value=[" "]):

        if type(value) is not list:
            print("value must be of type array")
            return None
        
        self.__value=list(value)
        
        # class attrinbute changing value
        Array.num_arrays+=1
        Array.array_arrays.append(self.__value)
        
    def set_value(self,new_value=[" "]):
        
        if type(new_value) is not list:
            print("new_value must be of type array")
            return None
        
        self.__value=list(new_value)
        
    def get_value(self):
        return self.__value

    def uppercase(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        new_array=[]
        for char in self.__value:
            
            if char in "abcdefghijklmnoqrstuvwyxz":
                new_array.append(char.upper())
            new_array.append(char)
            
        return new_array
    
    def lowercase(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        new_array=[]
        for char in self.__value:
            
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
                new_array.append(char.lower())
            new_array.append(char)
            
        return new_array

    def all_uppercase(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
                return False
        return True
    
    def all_lowercase(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        for char in self.__value:
            if char not in "abcdefghijklmnoqrstuvwyxz":
                return False
        return True
    
    def one_uppercase(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
                return True
        return False
    
    def one_lowercase(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        for char in self.__value:
            if char in "abcdefghijklmnoqrstuvwyxz":
                return True
        return False
    
    def all_alphabetic(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz":
                return False
        return True
    
    def one_alphabetic(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz":
                return True
        return False
    
   
    def concatonate(self,array2=[]):

        if type(array2) is not list:
            print("array2 must be of type array")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        return self.__value+list(array2)

    def all_numeric(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        for char in self.__value:
            if char not in "1234567890":
                return False
        return True
    
    def one_numeric(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        for char in self.__value:
            if char in "1234567890":
                return True
        return False    

    def all_alphanumeric(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz1234567890":
                return False
        return True
    
    def one_alphanumeric(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz1234567890":
                return True
        return False
    
    def length(self):

        length=0
        for char in self.__value:
            length+=1
        return length
    
    def is_subarray_of(self,array2=[]):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        if type(array2) is not list:
            print("array2 must be of type array")
            return None
        
        return self.__value in list(array2)

            
    def index(self,element=" "):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
        
        for i in range(len(self.__value)):
            if self.__value[i] ==element:
                return i
            
        return None

    def times_occured(self,element=" "):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        count=0

        for char in self.__value:
            if char == element:
                count+=1
        return count
    
    def remove_lowercase(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value :
            if char not in "abcdefghijklmnoqrstuvwyxz":
                array_string.append(char)
                
        return array_string
            
    def remove_uppercase(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
                array_string.append(char)

        return array_string

    
    def remove_numeric(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value:
            if char not in "1234567890":
                array_string.append(char)

        return array_string

    def remove_alphabetic(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz":
                array_string.append(char)

        return array_string

    def remove_alphanumeric(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz1234567890":
                array_string.append(char)
                
        return array_string
        
    def remove_nonuppercase(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
                array_string.append(char)

        return array_string
    
    def remove_nonlowercase(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value:
            if char in "abcdefghijklmnoqrstuvwyxz":
                array_string.append(char)

        return array_string
    
    def remove_nonnumeric(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value:
            if char in "1234567890":
                array_string.append(char)

        return array_string
    
    def remove_nonalphabetic(self):
        
        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz":
                array_string.append(char)
                
        return array_string
    
    def remove_nonalphanumeric(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz1234567890":
                array_string.append(char)

        return array_string
    
    def remove_spaces(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for char in self.__value:
            if not isinstance(char,str):
                print("all characters of self.__value must be of type str")
                return None
            
        array_string=[]
        
        for char in self.__value:
            if char not in [" ","\a","\b","\f","\n","\r","\t","\v"]:
                array_string.append(char)
            
        return array_string

    def slice(self,start=0,end=1):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        if (type(start) is not int) or (type(end) is not int):
            print("Start or end must be of type int")
            return None
        
        if(start < 0 or end>len(self.__value) ):
            print("start or end value out of range")
            return None
        
        array=[]
       
        for i in range(start,end):
            array.append(self.__value[i])
                  
        return array
    
    def reverse_order(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        array=[]
        for i in range(len(self.__value)-1,-1,-1):
            array.append(self.__value[i])
            
        return array
    
    def search(self,element=" "):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        array =[]
        for i in range(len(self.__value)):
            if self.__value[i] == element:
                array.append(i)
        return array
    
    def find_all(self,element =" "):

    
        array =[]
        for i in range(len(self.__value)):
            if self.__value[i] == element:
                array.append(self.__value[i])
        return array
    
    def maximum(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None

        all_num=True 
        for char in self.__value:
            if not isinstance(char,(int,float)):
                all_num=False

        all_str=True 
        for char in self.__value:
            if not isinstance(char,str):
                all_str=False
                    
        if (not all_num) and (not all_str):
            print("all characters in self.__value must be either all strings or all numbers")
            return None
        
        maximum =self.__value[0]
        for char in self.__value:
            if char> maximum:
                maximum = char
        return maximum
    
    def minimum(self):
        
        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None

        all_num=True 
        for char in self.__value:
            if not isinstance(char,(int,float)):
                all_num=False

        all_str=True 
        for char in self.__value:
            if not isinstance(char,str):
                all_str=False
                    
        if (not all_num) and (not all_str):
            print("all characters in self.__value must be either all strings or all numbers")
            return None
        
        minimum = self.__value[0]
        for char in self.__value:
            if char< minimum:
                minimum = char
        return minimum

    def mutate(self,index=0,element=" "):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        if type(index) is not int:
            print("index must be of type int")
            return None
        
        if index<0 or index>len(self.__value)-1:
            print("index value out of range")
            return None
        
        array_string = []
        for char in self.__value:
            array_string.append(char)
            
        for i in range(len(array_string)):
            if i == index:
                array_string[i] = element

        mutated_array=[]
        for char in array_string:
            mutated_array.append(char)
            
        return mutated_array
    
    def print_elements(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for i in range(len(self.__value)):
            print("Element at index "+ str(i) +" is "+ str(self.__value[i]))
            
    def print_element(self,index=0):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        if type(index) is not int:
            print("index must be of type int")
            return None
        
        if index<0 or index>len(self.__value)-1:
            print("index value out of range")
            return None
        
        for i in range(len(self.__value)):
            if i == index:
                print("Element at index "+ str(i) +" is "+ str(self.__value[i])+"\n")
                return None
            
    def add_array(self,array2=[]):

        if type(array2) is not list:
            print("array2 must be of type list")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        if len(self.__value) != len(array2):
            print("Both arrays must have the same length")
            return None

        new_array=[]
        for i in range(len(array2)):
            new_array.append(self.__value[i]+array2[i])
            
        return new_array

    def subtract_array(self,array2=[]):

        if type(array2) is not list:
            print("array2 must be of type list")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        if len(self.__value) != len(array2):
            print("Both arrays must have the same length")
            return None

        new_array=[]
        for i in range(len(array2)):
            new_array.append(self.__value[i]-array2[i])
            
        return new_array

    def multiply_array(self,array2=[]):

        if type(array2) is not list:
            print("array2 must be of type list")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        if len(self.__value) != len(array2):
            print("Both arrays must have the same length")
            return None

        new_array=[]
        for i in range(len(array2)):
            new_array.append(self.__value[i]*array2[i])
            
        return new_array
    
    def divide_array(self,array2=[]):

        if type(array2) is not list:
            print("array2 must be of type list")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        if len(self.__value) != len(array2):
            print("Both arrays must have the same length")
            return None

        new_array=[]
        for i in range(len(array2)):
            new_array.append(self.__value[i]/array2[i])
            
        return new_array
    
    def exponent_array(self,array2=[]):

        if type(array2) is not list:
            print("array2 must be of type list")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        if len(self.__value) != len(array2):
            print("Both arrays must have the same length")
            return None

        new_array=[]
        for i in range(len(array2)):
            new_array.append(self.__value[i]**array2[i])
            
        return new_array
    
    def modulus_array(self,array2=[]):

        if type(array2) is not list:
            print("array2 must be of type list")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        if len(self.__value) != len(array2):
            print("Both arrays must have the same length")
            return None

        new_array=[]
        for i in range(len(array2)):
            new_array.append(self.__value[i]%array2[i])
            
        return new_array
    
    def intdivide_array(self,array2=[]):

        if type(array2) is not list:
            print("array2 must be of type list")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        if len(self.__value) != len(array2):
            print("Both arrays must have the same length")
            return None
        
        new_array=[]
        for i in range(len(array2)):
            new_array.append(self.__value[i]//array2[i])
            
        return new_array
    
    def dot_product(self,array2):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        if type(array2) is not list:
            print("array2 must be of type list")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        if len(self.__value) != len(array2):
            print("Both arrays must have the same length")
            return None

        dot_product=0
        for i in range(len(array2)):
            dot_product+=self.__value[i]*array2[i]
            
        return dot_product

    def cross_product(self,array2):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        if type(array2) is not list:
            print("array2 must be of type list")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        if len(self.__value) != len(array2) and len(self.__value) == 3 and len(array2) == 3:
            print("Both arrays must have length 3")
            return None

        cross_product=[]
        cross_product.append(self.__value[1]*array2[2]-(self.__value[2]*array2[1]))
        cross_product.append(-(self.__value[0]*array2[2]-(self.__value[2]*array2[0])))
        cross_product.append(self.__value[0]*array2[1]-(self.__value[1]*array2[0]))

            
        return cross_product
    
    def add_elements(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        addition=0
        for i in range(len(self.__value)):
            addition+=self.__value[i]
            
        return addition

    def subtract_elements(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        subtraction=self.__value[0]
        for i in range(1,len(self.__value)):
            subtraction-=self.__value[i]
            
        return subtraction

    def multiply_elements(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        product=1
        for i in range(len(self.__value)):
            product*=self.__value[i]
            
        return product
    
    def divide_elements(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        divide=self.__value[0]
        for i in range(1,len(self.__value)):
            divide/=self.__value[i]
            
        return divide

    def modulus_elements(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        modulus=self.__value[0]
        for i in range(1,len(self.__value)):
            modulus+=self.__value[i]
            
        return modulus

    def intdivide_elements(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        intdivide=self.__value[0]
        for i in range(1,len(self.__value)):
            intdivide//=self.__value[i]
            
        return intdivide

    def avg_array(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        addition=0
        for i in range(len(self.__value)):
            addition+=self.__value[i]

        return addition/len(self.__value)
    
    def project_onto(self,array2=[]):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        if type(array2) is not list:
            print("array2 must be of type list")
            return None
        
        for char in array2:
            if not isinstance(char,(int,float)):
                print("all elements of array2 must be numbers")
                return None
            
        if len(self.__value) != len(array2):
            print("Both arrays must have the same length")
            return None

        dot_product=0
        for i in range(len(array2)):
            dot_product+=self.__value[i]*array2[i]

        squared_sum=0
        for i in range(len(array2)):
            squared_sum+=array2[i]**2

        squared_sum=abs(squared_sum)
        
        projection=[]
        for i in range(len(array2)):
            projection.append((dot_product/squared_sum)*array2[i])

        return projection

    def get_mode(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        element_to_count ={}
        elements=[]
        
        for element in self.__value:
            if element not in elements:
                element_to_count[element]=1
                elements.append(element)
            else:
                element_to_count[element]+=1
      
        
        mode=0
        maximum=0
        for element in elements:
            if element_to_count[element]>maximum:
                mode=element
                maximum=element_to_count[element]
                
            
        return mode
    
    def num_of_each_element(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        element_to_count ={}
        elements=[]
        
        for element in self.__value:
            if element not in elements:
                element_to_count[element]=1
                elements.append(element)
            else:
                element_to_count[element]+=1
                
        return element_to_count

    def get_median(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        i=1	
        median=0
        self.__value.sort()
		
        if len(self.__value) % 2 == 0:
            while i*2-len(self.__value)< 0:
                i+=1
				
            median = (self.__value[i-1]+self.__value[i])/2;
			
		
        elif len(self.__value)% 2 == 1:
			
            while i*2-len(self.__value)<0:
                i+=1
				
		
            median = self.__value[i-1]
            
        return median
    
    def get_lower_quartile(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
		
        k=0
        lower_quartile_values=[]
        self.__value.sort()
	
        if len(self.__value)%2==0:
          
            while k<len(self.__value)/2:
                lower_quartile_values.append(self.__value[k])
                k+=1
				
        elif len(self.__value)%2==1:
        
            while k<(len(self.__value)/2)-1:
                lower_quartile_values.append(self.__value[k]);
                k+=1
		
        lower_quartile = helper_functions.reusable_median(lower_quartile_values)

        return lower_quartile

    def get_upper_quartile(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        upper_quartile_values=[]
        self.__value.sort()
	
        if len(self.__value)%2==0:
            
            k=len(self.__value)/2
            
            while k<=len(self.__value)-1:
                upper_quartile_values.append(self.__value[k])
                k+=1
				
			
        elif len(self.__value)%2==1:
            
            k = int(len(self.__value)/2)+1
            
            while k<=len(self.__value)-1:
                upper_quartile_values.append(self.__value[k]);
                k+=1
		
        upper_quartile = helper_functions.reusable_median(upper_quartile_values)

        return upper_quartile

    def get_interquartile_range(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        self.__value.sort()

        lower_quartile = helper_functions.reusable_lower_quartile(self.__value)
        upper_quartile = helper_functions.reusable_upper_quartile(self.__value)

        interquartile_range = upper_quartile - lower_quartile
        
        return interquartile_range
    
    def get_pop_variance(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        count=0
        sum_values=0
        for integer in self.__value:
            sum_values+=integer
            count+=1;
			
			
        avg = sum_values/count
		
        avg_sum=0
        for integer in self.__value:
            
            avg_sum += (integer-avg)**2
			
        pop_variance=avg_sum/count
	
        return pop_variance

    def get_pop_standard_dev(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        count=0
        sum_values=0
        for integer in self.__value:
            sum_values+=integer
            count+=1;
			
			
        avg = sum_values/count
		
        avg_sum=0
        for integer in self.__value:
            
            avg_sum += (integer-avg)**2
			
        pop_standard_dev=math.sqrt(avg_sum/count)
	
        return pop_standard_dev

    def get_sample_variance(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        count=0
        sum_values=0
        for integer in self.__value:
            sum_values+=integer
            count+=1;
			
			
        avg = sum_values/count
		
        avg_sum=0
        for integer in self.__value:
            
            avg_sum += (integer-avg)**2
			
        sample_variance=avg_sum/(count-1)
	
        return sample_variance

    def get_sample_standard_dev(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        count=0
        sum_values=0
        for integer in self.__value:
            sum_values+=integer
            count+=1;
			
			
        avg = sum_values/count
		
        avg_sum=0
        for integer in self.__value:
            
            avg_sum += (integer-avg)**2
			
        sample_standard_dev=math.sqrt(avg_sum/(count-1))
	
        return sample_standard_dev

    		
    @classmethod
    def count_arrays(cls):
        return cls.num_arrays
    
    @classmethod
    def show_arrays(cls):
        return cls.array_arrays
    
    @classmethod
    def get_array(cls,num=1):
        
        if type(num) is not int:
            print("num must be if type int")
            return None
        
        if len(cls.array_arrays)==0:
            print("array_strings must not be empty")
            return None
        
        if num <1 or num > len(cls.array_arrays):
            print("num is out of range")
            return None
        
        for i in range(len(cls.array_arrays)):
            if i+1 == num:
                return cls.array_arrays[i]
            
      
    
    @staticmethod
    def explain_class():
        print("This class creates instances of the array object"+"\n"+\
              "It also defines methods that can be used perform common"+"\n"+\
              " operations on arrays")
