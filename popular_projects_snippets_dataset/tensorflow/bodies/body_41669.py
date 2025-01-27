# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
initial_value.append(random_ops.random_uniform((2, 3)))
exit(initial_value[0])
