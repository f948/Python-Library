import stringclass

stringclass.String.explain_class()

print(stringclass.String.count_strings())
print(stringclass.String.show_strings())

str1 = stringclass.String("$&#$")
str2 = stringclass.String("1RTTYY3")

# get_value()
print(str1.get_value())
print(str2.get_value())

# all_uppercase()
print(str1.all_uppercase())
print(str2.all_uppercase())

# all_lowercase()
print(str1.all_uppercase())
print(str2.all_uppercase())

# one_uppercase()
print(str1.one_uppercase())
print(str2.one_uppercase())

# one_lowercase()
print(str1.one_uppercase())
print(str2.one_uppercase())

# all_alphabetic()
print(str1.all_alphabetic())
print(str2.all_alphabetic())

# one_alphabetic()
print(str1.one_alphabetic())
print(str2.one_alphabetic())

# list_chars()
print(str1.list_chars())
print(str2.list_chars())

# concatonate()
print(str1.concatonate(str2))

# all_numeric()
print(str1.all_numeric())
print(str2.all_numeric())

# one_numeric()
print(str1.one_numeric())
print(str2.one_numeric())

# all_alphanumeric()
print(str1.all_alphanumeric())
print(str2.all_alphanumeric())

# one_alphanumeric()
print(str1.one_alphanumeric())
print(str2.one_alphanumeric())

# length()
print(str1.length())
print(str2.length())

# length()
print(str1.is_substring_of("123"))
print(str2.is_substring_of())

# index()
print(str1.index("a"))
print(str2.index("F"))

# times_occured()
print(str1.times_occured("a"))
print(str2.times_occured("F"))

# remove_lowercase()
print(str1.remove_lowercase())
print(str2.remove_lowercase())

# remove_uppercase()
print(str1.remove_uppercase())
print(str2.remove_uppercase())

# remove_numeric()
print(str1.remove_numeric())
print(str2.remove_numeric())

# remove_alphabetic()
print(str1.remove_alphabetic())
print(str2.remove_alphabetic())

# remove_alphanumeric()
print(str1.remove_alphanumeric())
print(str2.remove_alphanumeric())

# remove_alphanumeric()
print(str1.remove_alphanumeric())
print(str2.remove_alphanumeric())

# remove_nonuppercase()
print(str1.remove_nonuppercase())
print(str2.remove_nonuppercase())

# remove_spaces()
print(str1.remove_spaces())
print(str2.remove_spaces())

# slice()
print(str1.slice(0,3))
print(str2.slice(1,5))

print(stringclass.String.count_strings())
print(stringclass.String.show_strings())
print(stringclass.String.get_string(1))

# mutate()
print(str1.mutate(0,""))
print(str2.mutate(1,"2"))

# search()
print(str1.search("a"))
print(str2.search("F"))

# find_all()
print(str1.find_all("a"))
print(str2.find_all("F"))

str3 = stringclass.String("123")
str4 = stringclass.String("abc")

str5 = stringclass.String(" 23")
str6 = stringclass.String("a2c")

# maximum()
print(str5.maximum())
print(str6.maximum())

# minimum()
print(str3.minimum())
print(str4.minimum())

print(str1.print_elements())
print(str2.print_elements())

print(str1.print_element(0))
print(str2.print_element(1))
