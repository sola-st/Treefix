# Extracted from https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
from operator import attrgetter

# Will use a few data types to show a point
my_list = [1, "2", 3.0, [4], object(), type, None]

# I specifically want to create a generator
my_class_names = list(map(attrgetter("__name__"), map(type, my_list))))

# Result:
['int', 'str', 'float', 'list', 'object', 'type', 'NoneType']


# Alternatively, use a lambda
my_class_names = list(map(lambda x: type(x).__name__, my_list))

