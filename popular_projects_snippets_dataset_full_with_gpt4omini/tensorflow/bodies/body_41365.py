# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# The Reshape op requires the shape tensor to be placed in host memory.
reshape = polymorphic_function.function(array_ops.reshape)
value = constant_op.constant([1., 2.])
shape = constant_op.constant([2, 1]).gpu()
reshape(value, shape)  # No error is raised
