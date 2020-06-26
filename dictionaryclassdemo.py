import dictionaryclass

dictionaryclass.Dictionary.explain_class()
print(dictionaryclass.Dictionary.count_dictionaries())
print(dictionaryclass.Dictionary.show_dictionaries())

dictionary1 = dictionaryclass.Dictionary({2:2,2:2,2:2})
dictionary2 = dictionaryclass.Dictionary({6:6,6:6,6:6})

print(dictionary1.print_key_value_pairs())
print(dictionary2.print_key_value_pairs())

print(dictionary1.maximum_keys())
print(dictionary2.maximum_keys())

print(dictionary1.maximum_keys_if_value(2))
print(dictionary2.maximum_keys_if_value(6))

print(dictionary1.maximum_values_if_key(2))
print(dictionary2.maximum_values_if_key(6))

print(dictionary1.minimum_keys_if_value(2))
print(dictionary2.minimum_keys_if_value(6))

print(dictionary1.minimum_values_if_key(2))
print(dictionary2.minimum_values_if_key(6))

print(dictionary1.add_keys_if_value(2))
print(dictionary2.add_values_if_key(6))

print(dictionary1.length())
print(dictionary2.length())

print(dictionary1.avg_keys_if_value(2))
print(dictionary2.avg_values_if_key(6))

print(dictionary1.multiply_keys_if_value(2))
print(dictionary2.multiply_values_if_key(6))

print(dictionary1.median_keys_if_value(2))
print(dictionary2.median_values_if_key(6))

print(dictionary1.lower_quartile_keys())
print(dictionary2.lower_quartile_values())

print(dictionary1.lower_quartile_keys_if_value(2))
print(dictionary2.lower_quartile_values_if_key(6))

print(dictionary1.upper_quartile_keys_if_value(2))
print(dictionary2.upper_quartile_values_if_key(6))

print(dictionary1.interquartile_range_keys_if_value(2))
print(dictionary2.interquartile_range_values_if_key(6))

print(dictionary1.mode_keys_if_value(2))
print(dictionary2.mode_values_if_key(6))

print(dictionary1.pop_variance_keys_if_value(2))
print(dictionary2.pop_variance_values_if_key(6))

print(dictionary1.pop_standard_dev_keys_if_value(2))
print(dictionary2.pop_standard_dev_values_if_key(6))

print(dictionary1.sample_variance_keys_if_value(2))
print(dictionary2.sample_variance_values_if_key(6))

print(dictionary1.sample_standard_dev_keys_if_value(2))
print(dictionary2.sample_standard_dev_values_if_key(6))

print(dictionary1.projection_keys(dictionary2.get_value()))
print(dictionary2.projection_values(dictionary2.get_value()))

print(dictionary1.dot_product_keys(dictionary2.get_value()))
print(dictionary2.dot_product_values(dictionary2.get_value()))

print(dictionaryclass.Dictionary.count_dictionaries())
print(dictionaryclass.Dictionary.show_dictionaries())
print(dictionaryclass.Dictionary.get_dictionary(1))
print(dictionaryclass.Dictionary.get_dictionary(2))
