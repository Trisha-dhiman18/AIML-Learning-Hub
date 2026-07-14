# Check that a tuple type cannot be changed in python.
t1 = (1,2,3,4,5)
print(type(t1))
# t2 = str(t1)
# print(type(t2))
t1[0] = 10    #TypeError: 'tuple' object does not support item assignment
print(t1)