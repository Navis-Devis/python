# Python3 code to demonstrate working of
# Extract K digit Elements Tuples

# initializing list
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

# printing original list
print("The original list is : " + str(test_list))

# initialising K
K = 2

res=[]
for i in test_list:
	x=list(map(str,i))
	p=[]
	for j in x:
		p.append(len(j))
	if(p==[K,K] or p==[K]):
		res.append(i)
	
# printing result
print("The Extracted tuples : " + str(res))
