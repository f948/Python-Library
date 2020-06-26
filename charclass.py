
class Character:

    '''This class creates instances of the character object'''

    # class attributes 
    num_chars = 0
    array_chars =[]

    def __init__(self,value="a"):

        if type(value) is not str:
            print("value must be of type string")
            return None

        if len(value) != 1:
            print("char must have length 1")
            return None
        
        self.__value=str(value)

       
        # class attrinbute changing value
        Character.num_chars+=1
        Character.array_chars.append(self.__value)


    # object methods
    def set_value(self,new_value="a"):

        if type(value) is not str:
            print("value must be of type string")
            return None

        if len(value) != 1:
            print("char must have length 1")
            return None
        
        self.__value=str(new_value)
        
    def get_value(self):
        
        return self.__value
    
    def get_type(self):

        if self.__value in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return "uppercase alphabetic character"

        elif self.__value in "abcdefghijklmnopqrstuvwxyz":
            return "lowercase alphabetic character"
        
        elif self.__value in "0123456789":
            return "numeric character"

        elif self.__value in ["!","?",".",",","-","_"," "]:
            return "puncuational character"
        
        elif self.__value in ["\a","\b","\f","\n","\r","\t","\v"]:
            return "escape character"
        else:
            return"uncertain"
        
    def concatonate(self,char2="a"):

        if type(char2) is not str:
            print("char2 must be of type str ")
            return None
        
        return self.__value+char2
        
    @classmethod
    def count_chars(cls):
        return cls.num_chars
    
    @classmethod
    def show_chars(cls):
        return cls.array_chars
    
    @classmethod
    def get_chars(cls,num=1):

        if type(num) is not int:
            print("num must be of type int ")
            return None
        
        if len(cls.array_chars)==0:
            print("array_chars must not be empty")
            return None
        
        if num <1 or num > len(str(cls.array_chars)):
            print("num is out of range")
            return None
        
        for i in range(len(cls.array_chars)):
            if i+1 == num:
                return cls.array_chars[i]
            
    @staticmethod
    def explain_class():
        print("This class creates instances of the character object"+"\n"+\
              "It also defines methods that can be used perform commoun"+"\n"+\
              " operations on characters")
