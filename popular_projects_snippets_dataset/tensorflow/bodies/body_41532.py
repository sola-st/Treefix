# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
y = f(x, s=5)
assert y.shape.as_list() == [3, 5], y.shape.as_list()
exit(y)
