import helper_functions

class Dictionary:

    ''' This class creates instances of the dictionary object'''
    
    # class attributes
    num_dictionaries = 0
    array_dictionaries=[]
    
    def __init__(self,value={}):

        if type(value) is not dict:
            print("value must be of type dictionary")
            return None
        
        self.__value=dict(value)
        
       
        # class attrinbute changing value
        Dictionary.num_dictionaries+=1
        Dictionary.array_dictionaries.append(self.__value)
        
    def set_value(self,new_value={}):
        
        if type(new_value) is not dict:
            print("new_value must be of type dictionary")
            return None
        
        self.__value=dict(new_value)
        
    def get_value(self):
        return self.__value
    
    def get_key_from_value(self,value2=" "):

        for key in self.__value:
            if self.__value[key] == value2:
                return key
            
        return None
    
    def get_value_from_key(self,key2=" "):

        for key in self.__value:
            if key == key2:
                return self.__value[key]
            
        return None
    
    def length(self):

        length=0
        for key in self.__value:
            length+=1
        return length
    
    def maximum_keys(self):
        
        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
        
        maximum =-999999999999999
        for key in self.__value:
            if key> maximum:
                maximum = key
        return maximum

    def minimum_keys(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None
        
        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
        
        minimum =999999999999999
        for key in self.__value:
            if key< minimum:
                minimum= key
        return minimum

    def maximum_values(self):

        
        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        maximum =-999999999999999
        for key in self.__value:
            if self.__value[key]> maximum:
                maximum = self.__value[key]
        return maximum

    def minimum_values(self):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        minimum =999999999999999
        for key in self.__value:
            if self.__value[key]< minimum:
                minimum= self.__value[key]
        return minimum
    
    def maximum_keys_if_value(self,condition=" "):
        
        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
                
        maximum =-999999999999999
        for key in array:
            if key> maximum:
                maximum = key
        return maximum
    
    def minimum_keys_if_value(self,condition=" "):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
                
        minimum=999999999999999
        for key in array:
            if key< minimum:
                minimum = key
        return minimum
    
    def maximum_values_if_key(self,condition=" "):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
                
        maximum =-999999999999999
        for value in array:
            if value> maximum:
                maximum = value
                
        return maximum
    
    def minimum_values_if_key(self, condition=" "):

        if len(self.__value)==0:
            print("self.__value must not be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
                
        minimum=999999999999999
        for value in array:
            if value< minimum:
                minimum = value
                
        return minimum

    def add_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        sum_keys=0
        for key in self.__value:
            sum_keys+=key
            
        return sum_keys
    
    def avg_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        count=0
        sum_keys=0
        for key in self.__value:
            sum_keys+=key
            count+=1
            
        return sum_keys/count

    def add_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        sum_values=0
        for key in self.__value:
            sum_values+=self.__value[key]
        
            
        return sum_values
    
    def avg_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        count=0
        sum_values=0
        for key in self.__value:
            sum_values+=self.__value[key]
            count+=1
            
        return sum_values/count
    
    def add_keys_if_value(self,condition =" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
                
        sum_keys=0
        for key in array:
            sum_keys+=key
            
        return sum_keys

    def add_values_if_key(self,condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
                
        sum_values=0
        for value in array:
            sum_values+=value
            
        return sum_values

    def avg_keys_if_value(self,condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key]== condition:
                array.append(key)
                
        count=0
        sum_keys=0
        for key in array:
            sum_keys+=key
            count+=1
            
        return sum_keys/count

    def avg_values_if_key(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
                
        count=0
        sum_values=0
        for key in self.__value:
            sum_values+=self.__value[key]
            count+=1
            
        return sum_values/count

    def multiply_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        product_keys=1
        for key in self.__value:
            product_keys*=key
            
        return product_keys

    def multiply_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        product_values=1
        for key in self.__value:
            product_values*=self.__value[key]
            
        return product_values
    
    def multiply_keys_if_value(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
                
        product_keys=1
        for key in array:
            product_keys*=key
            
        return product_keys
    
    def multiply_values_if_key(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
                
        product_values=1
        for key in self.__value:
            product_values*=self.__value[key]
            
        return product_values
    
    def median_values_if_key(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
        
        array.sort()

        if len(array) == 1:
            return array[0]
        
        median=helper_functions.reusable_median(array)
        
        return median
    
    def median_keys_if_value(self,condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        median=helper_functions.reusable_median(array)
        
        return median

    def median_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        median=helper_functions.reusable_median(array)
        
        return median
    
    def median_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        median=helper_functions.reusable_median(array)
        
        return median

    def lower_quartile_keys_if_value(self,condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None
        
        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        lower_quartile=helper_functions.reusable_lower_quartile(array)
        
        return lower_quartile
    
    def lower_quartile_values_if_key(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        lower_quartile=helper_functions.reusable_lower_quartile(array)
        
        return lower_quartile
    
    def lower_quartile_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        lower_quartile=helper_functions.reusable_lower_quartile(array)
        
        return lower_quartile
    
    def lower_quartile_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        lower_quartile=helper_functions.reusable_lower_quartile(array)
        
        return lower_quartile

    def upper_quartile_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        upper_quartile=helper_functions.reusable_upper_quartile(array)
        
        return upper_quartile
    
    def upper_quartile_keys_if_value(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        upper_quartile=helper_functions.reusable_upper_quartile(array)
        
        return upper_quartile

    def upper_quartile_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        upper_quartile=helper_functions.reusable_upper_quartile(array)
        
        return upper_quartile
    
    def upper_quartile_values_if_key(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        upper_quartile=helper_functions.reusable_upper_quartile(array)
        
        return upper_quartile
    
    def interquartile_range_keys_if_value(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        lower_quartile = helper_functions.reusable_lower_quartile(array)
        upper_quartile = helper_functions.reusable_upper_quartile(array)

        interquartile_range = upper_quartile - lower_quartile
        
        return interquartile_range

    def interquartile_range_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        lower_quartile = helper_functions.reusable_lower_quartile(array)
        upper_quartile = helper_functions.reusable_upper_quartile(array)

        interquartile_range = upper_quartile - lower_quartile
        
        return interquartile_range
    
    def interquartile_range_values_if_key(self,condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        lower_quartile = helper_functions.reusable_lower_quartile(array)
        upper_quartile = helper_functions.reusable_upper_quartile(array)

        interquartile_range = upper_quartile - lower_quartile
        
        return interquartile_range

    def interquartile_range_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        lower_quartile = helper_functions.reusable_lower_quartile(array)
        upper_quartile = helper_functions.reusable_upper_quartile(array)

        interquartile_range = upper_quartile - lower_quartile
        
        return interquartile_range
    
    def mode_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(key)
            
        array.sort()

        mode=helper_functions.reusable_mode(array)

        return mode

    def mode_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(self.__value[key])
            
        array.sort()

        mode=helper_functions.reusable_mode(array)

        return mode
    
    def mode_keys_if_value(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
            
        array.sort()
 
        mode=helper_functions.reusable_mode(array)

        return mode
    
    def mode_values_if_key(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
            
        array.sort()

        mode=helper_functions.reusable_mode(array)

        return mode

    def pop_variance_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        pop_variance=functions.reusable_pop_variance(array)

        return pop_variance

    def pop_variance_keys_if_value(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        pop_variance=functions.reusable_pop_variance(array)

        return pop_variance
    
    def pop_variance_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        pop_variance=functions.reusable_pop_variance(array)

        return pop_variance
    
    def pop_variance_values_if_key(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        pop_variance=functions.reusable_pop_variance(array)

        return pop_variance
    
    def pop_standard_dev_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        pop_standard_dev=functions.reusable_pop_standard_dev(array)

        return pop_standard_dev

    def pop_standard_dev_keys_if_value(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        pop_standard_dev=functions.reusable_pop_standard_dev(array)

        return pop_standard_dev

    def pop_standard_dev_values_if_key(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        pop_standard_dev=functions.reusable_pop_standard_dev(array)

        return pop_standard_dev
    
    def pop_standard_dev_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        pop_standard_dev=functions.reusable_pop_standard_dev(array)

        return pop_standard_dev

    def sample_variance_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        sample_variance=functions.reusable_sample_variance(array)

        return sample_variance

    def sample_variance_keys_if_value(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        sample_variance=functions.reusable_sample_variance(array)

        return sample_variance

    def sample_variance_values_if_key(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if key == condition:
                array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        sample_variance=functions.reusable_sample_variance(array)

        return sample_variance
    
    def sample_variance_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        sample_variance=functions.reusable_sample_variance(array)

        return sample_variance

    def sample_standard_dev_keys(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        sample_standard_dev=functions.reusable_sample_standard_dev(array)

        return sample_standard_dev
    
    def sample_standard_dev_keys_if_value(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        sample_standard_dev=functions.reusable_sample_standard_dev(array)

        return sample_standard_dev

    def sample_standard_dev_values_if_key(self, condition=" "):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            if self.__value[key] == condition:
                array.append(key)
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        sample_standard_dev=functions.reusable_sample_standard_dev(array)

        return sample_standard_dev

    def sample_standard_dev_values(self):

        if len(self.__value) == 0:
            print("self.__value cannot be empty")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None
            
        array = []
        for key in self.__value:
            array.append(self.__value[key])
            
        array.sort()

        if len(array) == 1:
            return array[0]
        
        sample_standard_dev=functions.reusable_sample_standard_dev(array)

        return sample_standard_dev
    
    def projection_keys(self,dict2={1:2}):

        if type(dict2) is not dict:
            print("dict2 must of of type dict")
            return None
        
        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None

        for key in dict2:
            if not isinstance(key,(int,float)):
                print("all keys of dict2 must be numbers")
                return None
            
        if len(self.__value) != len(dict2):
            print("Both dictionaries must have the same length")
            return None

        vector_1 =[]
        for key in self.__value:
            vector_1.append(key)

        vector_2 =[]
        for key in dict2:
            vector_2.append(key)
            
        dot_product=0
        for i in range(len(vector_1)):
            dot_product+=vector_1[i]*vector_2[i]

        squared_sum=0
        for i in range(len(vector_2)):
            squared_sum+=vector_2[i]**2

        squared_sum=abs(squared_sum)
        
        projection=[]
        for i in range(len(vector_2)):
            projection.append((dot_product/squared_sum)*vector_2[i])

        return projection

    def projection_values(self,dict2={1:2}):

        if type(dict2) is not dict:
            print("dict2 must of of type dict")
            return None

        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None

        for key in dict2:
            if not isinstance(dict2[key],(int,float)):
                print("all values of dict2 must be numbers")
                return None
            
        if len(self.__value) != len(dict2):
            print("Both dictionaries must have the same length")
            return None

        vector_1 =[]
        for key in self.__value:
            vector_1.append(self.__value[key])

        vector_2 =[]
        for key in dict2:
            vector_2.append(dict2[key])
            
        dot_product=0
        for i in range(len(vector_1)):
            dot_product+=vector_1[i]*vector_2[i]

        squared_sum=0
        for i in range(len(vector_2)):
            squared_sum+=vector_2[i]**2

        squared_sum=abs(squared_sum)
        
        projection=[]
        for i in range(len(vector_2)):
            projection.append((dot_product/squared_sum)*vector_2[i])

        return projection
    
    def cross_product_keys(self,dict2={1:2}):

        if type(dict2) is not dict:
            print("dict2 must of of type dict")
            return None
        
        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None

        for key in dict2:
            if not isinstance(key,(int,float)):
                print("all keys of dict2 must be numbers")
                return None
            
        if len(self.__value) != len(dict2) and len(self.__value) == 3 and len(dict2) == 3:
            print("Both dictionaries must have length 3")
            return None

        vector_1 =[]
        for key in self.__value:
            vector_1.append(key)

        vector_2 =[]
        for key in dict2:
            vector_2.append(key)

        cross_product=[]
        cross_product.append(vector_1[1]*vector_2[2]-(vector_1[2]*vector_2[1]))
        cross_product.append(-(vector_1[0]*vector_2[2]-(vector_1[2]*vector_2[0])))
        cross_product.append(vector_1[0]*vector_2[1]-(vector_1[1]*vector_2[0]))

        return cross_product

    def cross_product_values(self,dict2={1:2}):

        if type(dict2) is not dict:
            print("dict2 must of of type dict")
            return None
        
        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None

        for key in dict2:
            if not isinstance(dict2[key],(int,float)):
                print("all values of dict2 must be numbers")
                return None
            
        if len(self.__value) != len(dict2) and len(self.__value) == 3 and len(dict2) == 3:
            print("Both dictionaries must have length 3")
            return None

        vector_1 =[]
        for key in self.__value:
            vector_1.append(self.__value[key])

        vector_2 =[]
        for key in dict2:
            vector_2.append(dict2[key])

        cross_product=[]
        cross_product.append(vector_1[1]*vector_2[2]-(vector_1[2]*vector_2[1]))
        cross_product.append(-(vector_1[0]*vector_2[2]-(vector_1[2]*vector_2[0])))
        cross_product.append(vector_1[0]*vector_2[1]-(vector_1[1]*vector_2[0]))

        return cross_product

    def dot_product_keys(self,dict2={1:2}):

        if type(dict2) is not dict:
            print("dict2 must of of type dict")
            return None
        
        for key in self.__value:
            if not isinstance(key,(int,float)):
                print("all keys of self.__value must be numbers")
                return None

        for key in dict2:
            if not isinstance(key,(int,float)):
                print("all keys of dict2 must be numbers")
                return None
            
        if len(self.__value) != len(dict2):
            print("Both dictionaries must have the same length")
            return None

        vector_1 =[]
        for key in self.__value:
            vector_1.append(key)

        vector_2 =[]
        for key in dict2:
            vector_2.append(key)
            
        dot_product=0
        for i in range(len(vector_1)):
            dot_product+=vector_1[i]*vector_2[i]
            
        return dot_product

    def dot_product_values(self,dict2={1:2}):

        if type(dict2) is not dict:
            print("dict2 must of of type dict")
            return None
        
        for key in self.__value:
            if not isinstance(self.__value[key],(int,float)):
                print("all values of self.__value must be numbers")
                return None

        for key in dict2:
            if not isinstance(dict2[key],(int,float)):
                print("all values of dict2 must be numbers")
                return None
            
        if len(self.__value) != len(dict2):
            print("Both dictionaries must have the same length")
            return None

        vector_1 =[]
        for key in self.__value:
            vector_1.append(self.__value[key])

        vector_2 =[]
        for key in dict2:
            vector_2.append(dict2[key])
            
        dot_product=0
        for i in range(len(vector_1)):
            dot_product+=vector_1[i]*vector_2[i]

        return dot_product
    
    def print_key_value_pairs(self):

        for key in self.__value:
            print("Key: "+str(key) + " Value: "+str(self.__value[key])+"\n")
        
    @classmethod
    def count_dictionaries(cls):
        return cls.num_dictionaries
    
    @classmethod
    def show_dictionaries(cls):
        return cls.array_dictionaries
    
    @classmethod
    def get_dictionary(cls,num=1):

        if type(num) is not int:
            print("num must be of type int")
            return None
        
        if len(cls.array_dictionaries)==0:
            print("array_dictionaries must not be empty")
            return None
        
        if num <1 or num > len(cls.array_dictionaries):
            print("num is out of range")
            return None
        
        for i in range(len(cls.array_dictionaries)):
            if i+1 == num:
                return cls.array_dictionaries[i]
            
        
    
    @staticmethod
    def explain_class():
        print("This class creates instances of the dictionary object"+"\n"+\
              "It also defines methods that can be used perform common"+"\n"+\
              " operations on dictionaries")
