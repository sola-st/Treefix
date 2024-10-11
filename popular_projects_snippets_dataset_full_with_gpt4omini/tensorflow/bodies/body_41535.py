# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
y = f(1, 2, 3)
assert y.shape.as_list() == [1, 2, 3], y.shape.as_list()
exit(y)
