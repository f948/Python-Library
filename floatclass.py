
class Float:

    ''' This class creates instances of the float number object'''
    
    # class attributes
    num_floats = 0
    array_floats=[]
    
    def __init__(self,value=1.0):

        if type(value) is not float:
            print("value must be of type float")
            return None
        
        self.__value=float(value)
      
       
        # class attrinbute changing value
        Float.num_floats+=1
        Float.array_floats.append(float(self.__value))
        
    # object methods
    def set_value(self,new_value=1.0):
        
        if type(value) is not float:
            print("value must be of type float")
            return None
        
        self.__value=float(new_value)
        
    def get_value(self):
        return self.__value
    
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
      
        
    def multiply(self,num2=1.0):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None
        
        return self.__value*num2
     
        
    def divide(self,num2=1.0):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None 
            
        if num2 == 0.0:
            print("Cannot divide by 0")
            return None
        
        return self.__value/num2
       
    
    def exponent(self,num2=1.0):

        if not isinstance(num2,(int,float)):
            print("num2 must be of type int or float")
            return None
        
        return self.__value**num2
    
    def num_digits(self):

        num_digits=0
        
        for char in str(self.__value):
            if char !=".":
                num_digits+=1
                
        return num_digits
    
    def list_digits(self):
        
        lst_digits=[]
        for digit in str(self.__value):
            if digit !=".":
                lst_digits.append(int(digit))
        return lst_digits
    
    @classmethod
    def count_floats(cls):
        return cls.num_floats
    
    @classmethod
    def show_floats(cls):
        return cls.array_floats
    
    @classmethod
    def get_float(cls,num=1):
        
        if len(cls.array_floats)==0:
            print("array_floats must not be empty")
            return None

        if type(num) is not int:
            print("num must be an integer")
            return None 
                  
        if num <1 or num > len(str(cls.array_floats)):
            print("num is out of range")
            return None
        
        for i in range(len(cls.array_floats)):
            if i+1 == num:
                return cls.array_floats[i]
            
    @staticmethod
    def explain_class():
        print("This class creates instances of the float object"+"\n"+\
              "It also defines methods that can be used perform common"+"\n"+\
              " operations on floats")
