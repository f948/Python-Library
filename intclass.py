import helper_functions

class Int:

    ''' This class creates instances of the integer object'''
    
    # class attributes
    num_ints = 0
    array_ints=[]
    
    def __init__(self,value=1,convertable=True):

        if type(value) is not int:
            print("value must be of type int")
            return None
        
        if type(convertable) is not bool:
            print("convertable must be of type bool")
            return None
        
        self.__value=int(value)
        self.__convertable= bool(convertable)
       
        # class attrinbute changing value
        Int.num_ints+=1
        Int.array_ints.append(self.__value)
        
    # object methods
    def set_value(self,new_value=1):

        if type(value) is not int:
            print("value must be of type int")
            return None
        
        self.__value=int(new_value)
        
    def get_value(self):
        return self.__value
    
    def set_convertable(self,new_convertable):

        if type(convertable) is not bool:
            print("convertable must be of type bool")
            return None
        
        self.__convertable=bool(new_convertable)
        
    def get_convertable(self):
        return self.__convertable
    
    def add(self,num2=0):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None
        
        return self.__value+num2
       
        
    def subtract(self,num2=0):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None
        
        return self.__value-num2
      
        
    def multiply(self,num2=1):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None
        
        return self.__value*num2
     
        
    def divide(self,num2=1):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None
        
        if num2 == 0:
            print("Cannot divide by 0")
            return None
        
        return self.__value/num2
       
        
    def modulus(self,num2=1):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None
        
        return self.__value%num2
        
        
    def exponent(self,num2=1):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None
        
        return self.__value**num2
    
        
    def int_divide(self,num2=1):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None
        
        if num2 == 0:
            print("Cannot divide by 0")
            return None
        
        return self.__value//num2
       
    def divisible_by(self,num2=1):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None
        
        if num2 == 0:
            print("Cannot divide by 0")
            return None
        
        if self.__value%num2==0:
            return True
        else:
            return False 
            
    def get_length(self):
        
        length = 0
        for char in str(self.__value):
            length+=1
        return length
    
    def get_digit(self,num=1):

        if type(num) is not int:
            print("num must be of type int ")
            return None
        
        if num <1 or num > len(str(self.__value)):
            print("Num is out of range")
            return None
        
        for i in range(len(str(self.__value))):
            if i+1 == num:
                return int(str(self.__value)[i])
            
        return None

    def convert_to_binary(self):

        if self.__value < 0:
            print("Integer must be positive or 0")
            return None
        
        if self.__convertable:
            binary=""
            integer = self.__value
       
            while integer>0:
                binary+=str(integer%2)
                integer=integer//2
            
            return binary[::-1]
        else:
            print("self.__convertable must be true")
            return None 
    
    def convert_to_octal(self):

        if self.__value < 0:
            print("Integer must be positive or 0")
            return None
        
        if self.__convertable:
            octal=""
            integer = self.__value
        
            while integer>0:
                octal+=str(integer%8)
                integer=integer//8
            
    
            return octal[::-1]
        else:
            print("self.__convertable must be true")
            return None 

    def convert_to_hexadecimal(self):

        if self.__value < 0:
            print("Integer must be positive or 0")
            return None
        
        if self.__convertable:
            HEXADECIMAL_CHARACTERS=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
            hexadecimal=""
            integer = self.__value
        
            while integer>0:
                hexadecimal+=str(HEXADECIMAL_CHARACTERS[integer%16])
                integer=integer//16
            
    
            return hexadecimal[::-1]
        else:
            print("self.__convertable must be true")
            return None
        
    def get_factorial(self):

        if type(self.__value) is not int:
            print("self.__value must be of type integer")
            return None
        
        if self.__value <= 0:
            print("self.__value must be positive")
            return None

        factorial = 1
        for factor in range(self.__value,0,-1):
            factorial*=factor

        return factorial

    def get_permutation_of(self,r=1):

        if type(self.__value) is not int:
            print("self.__value must be of type integer")
            return None

        if type(r) is not int:
            print("r must be of type integer")
            return None
        
        if self.__value <= 0:
            print("self.__value must be positive")
            return None

        if r <= 0:
            print("r must be positive")
            return None
        
        if int(self.__value-r)<=0:
            print("self.__value > r must be true")
            return None
        
        return helper_functions.factorial(self.__value)/(helper_functions.factorial(int(self.__value-r)))

    def get_combination_of(self,r=1):

        if type(self.__value) is not int:
            print("self.__value must be of type integer")
            return None

        if type(r) is not int:
            print("r must be of type integer")
            return None
        
        if self.__value <= 0:
            print("self.__value must be positive")
            return None

        if r <= 0:
            print("r must be positive")
            return None

        if int(self.__value-r)<=0:
            print("self.__value > r must be true")
            return None
        
        return int(helper_functions.factorial(self.__value))//(helper_functions.factorial(int(self.__value-r))*helper_functions.factorial(r))
    
    def list_digits(self):
        
        lst_digits=[]
        for digit in str(self.__value):
            lst_digits.append(int(digit))
        return lst_digits
    
    def num_digits(self):
        
        num_digits=0
        
        for char in str(self.__value):
            num_digits+=1
                
        return num_digits

    def print_digits(self):

        for i in range(len(str(self.__value))):
            print("Element at index "+ str(i) +" is "+ str(self.__value)[i])
            
    def print_digit(self,index=0):

        if index<0 or index>len(str(self.__value))-1:
            print("index value out of range")
            return None
        
        for i in range(len(str(self.__value))):
            if i == index:
                print("Digit at index "+ str(i) +" is "+ str(self.__value)[i]+"\n")
                return None
            
    @classmethod
    def count_ints(cls):
        return cls.num_ints
    
    @classmethod
    def show_ints(cls):
        return cls.array_ints
    
    @classmethod
    def get_int(cls,num=1):

        if type(num) is not int:
            print("num must be of type int ")
            return None
        
        if len(cls.array_ints)==0:
            print("array_ints must not be empty")
            return None
        
        if num <1 or num > len(str(cls.array_ints)):
            print("num is out of range")
            return None
        
        for i in range(len(cls.array_ints)):
            if i+1 == num:
                return cls.array_ints[i]
    
    @classmethod
    def explain_class(cls):
        print("This class creates instances of the integer object"+"\n"+\
              "It also defines methods that can be used perform common"+"\n"+\
              " operations on integers")
        
