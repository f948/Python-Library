import intclass

intclass.Int.explain_class()

print(intclass.Int.count_ints())
print(intclass.Int.show_ints())

# creating instances of the Int object
int1 = intclass.Int(0)
int2 = intclass.Int(16)

int3 = intclass.Int(33)
int4 = intclass.Int(21)

# get_factorial()
print(int1.get_factorial())
print(int2.get_factorial())

# get_permutation_of()
print(int1.get_permutation_of(2))
print(int2.get_permutation_of(1))

# get_combination_of()
print(int1.get_combination_of(2))
print(int2.get_combination_of(1))


print(int1.get_digit(1))
print(int2.get_digit(1))

print(int1.divisible_by(1))
print(int1.divisible_by(10))

print(int2.divisible_by(1))
print(int2.divisible_by(10))

print(int1.convert_to_binary())
print(int2.convert_to_binary())

print(int1.convert_to_octal())
print(int2.convert_to_octal())

print(int1.convert_to_hexadecimal())
print(int2.convert_to_hexadecimal())
print(int3.convert_to_hexadecimal())
print(int4.convert_to_hexadecimal())

print(int1.num_digits())
print(int2.num_digits())

print(int1.print_digits())
print(int2.print_digits())

print(int1.print_digit(0))
print(int2.print_digit(0))

# performing operations 
print(int1.add(int2.get_value()))
print(int1.subtract(int2.get_value()))
print(int1.multiply(int2.get_value()))
print(int1.divide(int2.get_value()))
print(int1.exponent(int2.get_value()))
print(int1.modulus(int2.get_value()))
print(int1.int_divide(int2.get_value()))

# other methods 
print(int1.get_length())
print(int2.get_length())

print(int1.get_digit(1))
print(int2.get_digit(1))


print(int1.list_digits())
print(int2.list_digits())

print(int1.num_digits())
print(int2.num_digits())

print(intclass.Int.count_ints())
print(intclass.Int.show_ints())

print(intclass.Int.get_int(1))
print(intclass.Int.get_int(2))
