# Python3 code to demonstrate working of
# Uppercase Half String
# Using upper() + slicing string

# initializing string
test_str = 'Navedspracticecode'

# printing original string
print("The original string is : " + str(test_str))

# computing half index
hlf_idx = len(test_str) // 2

# Making new string with half upper case
# Using slicing
# slicing takes one position less to ending position provided
res = test_str[:hlf_idx] + test_str[hlf_idx:].upper()

# printing result
print("The resultant string : " + str(res))
