# Extracted from https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
func_name = 'reverse'

l = [1, 2, 3, 4]
print(l)
>> [1, 2, 3, 4]

l.__getattribute__(func_name)()
print(l)
>> [4, 3, 2, 1]

