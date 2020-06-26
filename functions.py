import math

def reusable_median(sorted_array):

    i=1	
    median=0
    
    if len(sorted_array) % 2 == 0:
        while i*2-len(sorted_array)< 0:
            i+=1
				
        median = (sorted_array[i-1]+sorted_array[i])/2;
			
		
    elif len(sorted_array)% 2 == 1:
			
        while i*2-len(sorted_array)<0:
            i+=1
				
		
        median = sorted_array[i-1]
            
    return median

def reusable_lower_quartile(sorted_array):
    
    k=0
    lower_quartile_values=[]
        
	
    if len(sorted_array)%2==0:
          
        while k<len(sorted_array)/2:
            lower_quartile_values.append(sorted_array[k])
            k+=1
				
    elif len(sorted_array)%2==1:
        
        while k<(len(sorted_array)/2)-1:
            lower_quartile_values.append(sorted_array[k]);
            k+=1
		
    lower_quartile = reusable_median(lower_quartile_values)

    return lower_quartile

def reusable_upper_quartile(sorted_array):

    upper_quartile_values=[]
     
    if len(sorted_array)%2==0:
            
        k=int(len(sorted_array)/2)
            
        while k<=int(len(sorted_array)-1):
            upper_quartile_values.append(sorted_array[k])
            k+=1
				
			
    elif len(sorted_array)%2==1:
            
        k = int(len(sorted_array)/2)+1
            
        while k<=len(sorted_array)-1:
            upper_quartile_values.append(sorted_array[k]);
            k+=1
		
    upper_quartile = reusable_median(upper_quartile_values)

    return upper_quartile

def reusable_mode(sorted_array):

    element_to_count ={}
    elements=[]
        
    for element in sorted_array:
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

def reusable_pop_variance(array):

    if len(array) == 0:
        print("self.__value cannot be empty")
        return None
        
    count=0
    sum_values=0
    for integer in array:
        sum_values+=integer
        count+=1;
			
			
    avg = sum_values/count
		
    avg_sum=0
    for integer in array:
            
        avg_sum += (integer-avg)**2
			
    pop_variance=avg_sum/count
	
    return pop_variance

def reusable_pop_standard_dev(array):

    if len(array) == 0:
        print("self.__value cannot be empty")
        return None
        
    count=0
    sum_values=0
    for integer in array:
        sum_values+=integer
        count+=1;
			
			
    avg = sum_values/count
		
    avg_sum=0
    for integer in array:
            
        avg_sum += (integer-avg)**2
			
    pop_standard_dev=math.sqrt(avg_sum/count)
	
    return pop_standard_dev

def reusable_sample_variance(array):

    if len(array) == 0:
        print("self.__value cannot be empty")
        return None
        
    count=0
    sum_values=0
    for integer in array:
        sum_values+=integer
        count+=1;
			
			
    avg = sum_values/count
		
    avg_sum=0
    for integer in array:
            
        avg_sum += (integer-avg)**2
			
    sample_variance=avg_sum/(count-1)
	
    return sample_variance

def reusable_sample_standard_dev(array):

    if len(array) == 0:
        print("self.__value cannot be empty")
        return None
        
    count=0
    sum_values=0
    for integer in array:
        sum_values+=integer
        count+=1;
			
			
    avg = sum_values/count
		
    avg_sum=0
    for integer in array:
            
        avg_sum += (integer-avg)**2
			
    sample_standard_dev=math.sqrt(avg_sum/(count-1))
	
    return sample_standard_dev


