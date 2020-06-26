import floatclass

floatclass.Float.explain_class()

print(floatclass.Float.count_floats())
print(floatclass.Float.show_floats())

# creating instances of the Float object
float1 = floatclass.Float(13.45)
float2 = floatclass.Float(2.5687)

print(float1.num_digits())
print(float2.num_digits())

# performing operations 
print(float1.add(float2.get_value()))
print(float1.subtract(float2.get_value()))
print(float1.multiply(float2.get_value()))
print(float1.divide(float2.get_value()))
print(float1.exponent(float2.get_value()))


print(floatclass.Float.count_floats())
print(floatclass.Float.show_floats())

print(floatclass.Float.get_float(1))
print(floatclass.Float.get_float(2))
