import arrayclass

arrayclass.Array.explain_class()

print(arrayclass.Array.count_arrays())
print(arrayclass.Array.show_arrays())

array1 = arrayclass.Array(["g","d","R","h","d","n"])
array2 = arrayclass.Array([1,2,3,4,5])

array3 = arrayclass.Array(["g","d",1.0,True,"d",1])
array4 = arrayclass.Array([1,True,1.0,4,"#$%"])

print(array1.maximum())
print(array2.maximum())

print(array1.minimum())
print(array2.minimum())

print(array3.minimum())
print(array4.minimum())

# search()
print(array1.search("R"))
print(array2.search(5))

# find_all()
print(array1.find_all("R"))
print(array2.find_all(5))

# get_value()
print(array1.get_value())
print(array2.get_value())

# all_uppercase()
print(array1.all_uppercase())
print(array2.all_uppercase())

# one_uppercase()
print(array1.one_uppercase())
print(array2.one_uppercase())

# all_lowercase()
print(array1.one_lowercase())
print(array2.one_lowercase())

# one_lowercase()
print(array1.one_lowercase())
print(array2.one_lowercase())

# all_alphabetic()
print(array1.all_alphabetic())
print(array2.all_alphabetic())

# one_alphabetic()
print(array1.one_alphabetic())
print(array2.one_alphabetic())

# concatonate()
print(array1.concatonate(["1","2","3"]))
print(array2.concatonate(["#","78","@$%3"]))

# all_numeric()
print(array1.all_numeric())
print(array2.all_numeric())

# one_numeric()
print(array1.one_numeric())
print(array2.one_numeric())

# all_alphanumeric()
print(array1.all_alphanumeric())
print(array2.all_alphanumeric())

# one_alphanumeric()
print(array1.one_alphanumeric())
print(array2.one_alphanumeric())

# length()
print(array1.length())
print(array2.length())

# length()
print(array1.is_subarray_of([]))
print(array2.is_subarray_of(["1","@","#"]))

# index()
print(array1.index("\n"))
print(array2.index(":"))

# times_occured()
print(array1.times_occured("\n"))
print(array2.times_occured(":"))

# remove_lowercase()
print(array1.remove_lowercase())
print(array2.remove_lowercase())

# remove_uppercase()
print(array1.remove_uppercase())
print(array2.remove_uppercase())

# remove_numeric()
print(array1.remove_numeric())
print(array2.remove_numeric())

# remove_alphabetic()
print(array1.remove_alphabetic())
print(array2.remove_alphabetic())

# remove_alphanumeric()
print(array1.remove_alphanumeric())
print(array2.remove_alphanumeric())

# remove_alphanumeric()
print(array1.remove_alphanumeric())
print(array2.remove_alphanumeric())

# remove_nonuppercase()
print(array1.remove_nonuppercase())
print(array2.remove_nonuppercase())

# remove_spaces()
print(array1.remove_spaces())
print(array2.remove_spaces())

# slice()
print(array1.slice(0,3))
print(array2.slice(1,5))

print(arrayclass.Array.count_arrays())
print(arrayclass.Array.show_arrays())
print(arrayclass.Array.get_array(1))

# mutate()
print(array1.mutate(0,"WEW"))
print(array2.mutate(1,"2"))

# maximum()
print(array1.maximum())
print(array2.maximum())

# minimum()
print(array1.minimum())
print(array2.minimum())

array3 = arrayclass.Array([1,2,3])
array4 = arrayclass.Array([4,5,6])

print(array3.project_onto(array4.get_value()))
      
print(array3.dot_product(array4.get_value()))
print(array3.cross_product(array4.get_value()))

print(array3.add_array(array4.get_value()))
print(array3.subtract_array(array4.get_value()))

print(array3.multiply_array(array4.get_value()))
print(array3.divide_array(array4.get_value()))

print(array3.exponent_array(array4.get_value()))
print(array3.modulus_array(array4.get_value()))

print(array3.intdivide_array(array4.get_value()))

array5= arrayclass.Array([1,2,3,4,5])

print(array5.get_median())

print(array5.get_lower_quartile())
print(array5.get_upper_quartile())
print(array5.get_interquartile_range())

print(array5.get_pop_variance())
print(array5.get_sample_variance())

print(array5.get_pop_standard_dev())
print(array5.get_sample_standard_dev())

print(array5.get_mode())
print(array5.num_of_each_element())

array5.print_elements()
array5.print_element(1)
array5.print_element(0)
