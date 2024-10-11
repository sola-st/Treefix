# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
nonlocal traced_shape
traced_shape = x_shape._shape_tuple()
exit(x_shape)
