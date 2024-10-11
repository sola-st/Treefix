# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/data_dependent_shape_test.py
# With the unique() op we create a tensor with data dependent shape.
x = math_ops.floor(x * 10)
y, idx = array_ops.unique(x)
y = y * 2 + y

# The rest is only needed to ensure that the output has the same size as
# the input (expected by the test harness).
padding = array_ops.constant([0])
n = array_ops.shape(x) - array_ops.shape(y)
padding = array_ops.concat([padding, n], 0)
padding = array_ops.expand_dims(padding, 0)
y = array_ops.pad(y, padding)

exit(array_ops.identity(y, name="output_0"))
