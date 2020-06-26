
class String:

    ''' This class creates instances of the string object'''
    
    # class attributes
    num_strings = 0
    array_strings=[]
    
    def __init__(self,value=" "):

        if type(value) is not str:
            print("value must be of type str")
            return None
        
        if len(value) == 1:
            print("object should be created from Character class")
            return None
        
        self.__value=str(value)
        
        # class attrinbute changing value
        String.num_strings+=1
        String.array_strings.append(self.__value)
        
    def set_value(self,new_value=" "):

        if type(new_value) is not str:
            print("new_value must be of type str")
            return None
        
        if len(new_value) == 1:
            print("object should be created from Character class")
            return None
        
        self.__value=str(new_value)
        
    def get_value(self):
        return self.__value

    def uppercase(self):
        
        new_string=""
        for char in self.__value:
            
            if char in "abcdefghijklmnoqrstuvwyxz":
                new_string+=char.upper()
            else:
                new_string+=char
            
        return new_string
    
    def lowercase(self):

        new_string=""
        for char in self.__value:
            
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
                new_string+=char.lower()
            else:
                new_string+=char
            
        return new_string

    def all_uppercase(self):

        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
                return False
        return True
    
    def all_lowercase(self):

        for char in self.__value:
            if char not in "abcdefghijklmnoqrstuvwyxz":
                return False
        return True
    
    def one_uppercase(self):

        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
                return True
        return False
    
    def one_lowercase(self):

        for char in self.__value:
            if char in "abcdefghijklmnoqrstuvwyxz":
                return True
        return False
    
    def all_alphabetic(self):

        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz":
                return False
        return True
    
    def one_alphabetic(self):

        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz":
                return True
        return False
    
    def list_chars(self):
        
        lst=[]
        for char in self.__value:
            lst.append(char)
            
        return lst
    
   
    def concatonate(self,str2=" "):

        if type(str2) is not str:
            print("str2 must be of type str ")
            return None

        return self.__value+str(str2)

    def all_numeric(self):
        
        for char in self.__value:
            if char not in "1234567890":
                return False
        return True
    
    def one_numeric(self):
        
        for char in self.__value:
            if char in "1234567890":
                return True
        return False    

    def all_alphanumeric(self):
        
        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz1234567890":
                return False
        return True
    
    def one_alphanumeric(self):

        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz1234567890":
                return True
        return False
    
    def length(self):

        length=0
        for char in self.__value:
            length+=1
        return length
    
    def is_substring_of(self,str2=" "):

        if type(str2) is not str:
            print("str2 must be of type str ")
            return None
        
        return self.__value in str(str2)

    
    def index(self,char2=" "):
        
        if type(char2) is not str:
            print("char2 must be of type str ")
            return None
        
        if len(char2) != 1:
            print("char2 must have length 1")
            return None
        
        for i in range(len(self.__value)):
            if self.__value[i] == str(char2):
                return i
            
        return None

    def times_occured(self,char2=" "):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
         
        if type(char2) is not str:
            print("char2 must be of type str ")
            return None

        if len(char2) != 1:
            print("char2 must have length 1")
            return None
        
        count=0

        for char in self.__value:
            if char == str(char2):
                count+=1
        return count
    
    def remove_lowercase(self):
   
        lst_string=[]
        
        for char in self.__value :
            if char not in "abcdefghijklmnoqrstuvwyxz":
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string
            
    def remove_uppercase(self):
      
        lst_string=[]
        
        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string

    
    def remove_numeric(self):

        lst_string=[]
        
        for char in self.__value:
            if char not in "1234567890":
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string

    def remove_alphabetic(self):

        lst_string=[]
        
        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz":
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string

    def remove_alphanumeric(self):

        lst_string=[]
        
        for char in self.__value:
            if char not in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz1234567890":
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string
        
    def remove_nonuppercase(self):

        lst_string=[]
        
        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string

    def remove_nonlowercase(self):

        lst_string=[]
        
        for char in self.__value:
            if char in "abcdefghijklmnoqrstuvwyxz":
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string
    
    def remove_nonnumeric(self):

        lst_string=[]
        
        for char in self.__value:
            if char in "1234567890":
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string
    
    def remove_nonalphabetic(self):

        lst_string=[]
        
        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz":
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string
    
    def remove_nonalphanumeric(self):

        lst_string=[]
        
        for char in self.__value:
            if char in "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwyxz1234567890":
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string
    
    def remove_spaces(self):

        lst_string=[]
        
        for char in self.__value:
            if char not in [" ","\a","\b","\f","\n","\r","\t","\v"]:
                lst_string.append(char)

        new_string=""
        for element in lst_string:
            new_string+=element
            
        return new_string

    def slice(self,start=0,end=1):

        if (type(start) is not int) or (type(end) is not int):
            print("Start or end must be of type int")
            return None
        
        if(start < 0 or end>len(self.__value) ):
            print("start or end value out of range")
            return None
        
        string=""
       
        for i in range(start,end):
            string+=self.__value[i]
                  
        return string
    
    def reverse_order(self):
        
        string=""
        for i in range(len(self.__value)-1,-1,-1):
            string+=self.__value[i]
            
        return string
        
    def search(self,char2=" "):

        if type(char2) is not str:
            print("char2 must be of type str ")
            return None
        
        if len(str(char2)) != 1:
            print("char2 must be a one character string")
            return None
        
        lst =[]
        for i in range(len(self.__value)):
            if self.__value[i] == str(char2):
                lst.append(i)
        return lst
    
    def find_all(self,char2=" "):

        if type(char2) is not str:
            print("char2 must be of type str ")
            return None
        
        if len(str(char2)) != 1:
            print("char2 must be a one character string")
            return None
        
        lst =[]
        for i in range(len(self.__value)):
            if self.__value[i] == str(char2):
                lst.append(self.__value[i])
        return lst
    
    def maximum(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None

        all_alphabetic=True 
        for char in self.__value:
            if not char.isalpha():
                all_alphabetic=False

        all_numeric=True 
        for char in self.__value:
            if not char.isnumeric():
                all_numeric=False
                    
        if (not all_alphabetic) and (not all_numeric):
            print("all characters in self.__value must be either all alphabetic or all numeric")
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
        
        all_alphabetic=True 
        for char in self.__value:
            if not char.isalpha():
                all_alphabetic=False

        all_numeric=True 
        for char in self.__value:
            if not char.isnumeric():
                all_numeric=False
                    
        if (not all_alphabetic) and (not all_numeric):
            print("all characters in self.__value must be either all alphabetic or all numeric")
            return None 
        
        minimum = self.__value[0]
        for char in self.__value:
            if char< minimum:
                minimum = char
        return minimum
    
    def mutate(self,index=0,char2=" "):

        if type(char2) is not str:
            print("char2 must be of type str ")
            return None
        
        if index<0 or index>len(self.__value)-1:
            print("index value out of range")
            return None
        
        if len(char2) != 1:
            print("char2 must have length 1")
            return None

        lst_string = []
        for char in self.__value:
            lst_string.append(char)
            
        for i in range(len(lst_string)):
            if i == index:
                lst_string[i] = char2

        mutated_string=""
        for char in lst_string:
            mutated_string+=char
            
        return mutated_string
    
    def print_elements(self):

        for i in range(len(self.__value)):
            print("Element at index "+ str(i) +" is "+ str(self.__value[i]))
            
    def print_element(self,index=0):

        if type(index) is not int:
            print("index must be of type int ")
            return None
        
        if index<0 or index>len(self.__value)-1:
            print("index value out of range")
            return None
        
        for i in range(len(self.__value)):
            if i == index:
                print("Element at index "+ str(i) +" is "+ str(self.__value[i])+"\n")
                return None
            
    @classmethod
    def count_strings(cls):
        return cls.num_strings
    
    @classmethod
    def show_strings(cls):
        return cls.array_strings
    
    @classmethod
    def get_string(cls,num=1):

        if type(num) is not int:
            print("num must be of type int ")
            return None
        
        if len(cls.array_strings)==0:
            print("array_strings must not be empty")
            return None
        
        if num <1 or num > len(cls.array_strings):
            print("num is out of range")
            return None
        
        for i in range(len(cls.array_strings)):
            if i+1 == num:
                return cls.array_strings[i]
            
        
    
    @staticmethod
    def explain_class():
        print("This class creates instances of the string object"+"\n"+\
              "It also defines methods that can be used perform common"+"\n"+\
              " operations on strings")
