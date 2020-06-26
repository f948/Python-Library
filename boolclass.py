
class Boolean:

    '''This class creates instances of the boolean variables object'''

    # class attributes 
    num_bools = 0
    array_bools =[]

    def __init__(self,value=True):

        if type(value) is not bool:
            print("value must be of type bool")
            return None
        
        self.__value=bool(value)

       
        # class attrinbute changing value
        Boolean.num_bools+=1
        Boolean.array_bools.append(self.__value)


    # object methods
    def set_value(self,new_value=True):

        if type(value) is not bool:
            print("value must be of type bool")
            return None
        
        self.__value=bool(new_value)
        
    def get_value(self):
        
        return self.__value

    def is_not(self):

        return not self.__value
    
    @classmethod
    def count_bools(cls):
        return cls.num_bools
    
    @classmethod
    def show_bools(cls):
        return cls.array_bools
    
    @classmethod
    def get_bool(cls,num=1):

        if type(num) is not int:
            print("num must be of type int")
            return None
        
        if len(cls.array_bools)==0:
            print("array_bools must not be empty")
            return None
        
        if num <1 or num > len(str(cls.array_bools)):
            print("num is out of range")
            return None
        
        for i in range(len(cls.array_bools)):
            if i+1 == num:
                return cls.array_bools[i]
            
     
    
    @staticmethod
    def explain_class():
        print("This class creates instances of the boolean variable object"+"\n"+\
              "It also defines methods that can be used perform commoun"+"\n"+\
              " operations on boolean variables")
