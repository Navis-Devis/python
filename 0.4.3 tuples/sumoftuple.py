# Python3 code to demonstrate working of
# Tuple summation

# Initializing tuple
test_tup = (7, 8, 9, 1, 10, 7)

# Printing original tuple
print("The original tuple is : " + str(test_tup))

res = 0
for i in test_tup:
	res += i

# Printing result
print("The summation of tuple elements are : " + str(res))
