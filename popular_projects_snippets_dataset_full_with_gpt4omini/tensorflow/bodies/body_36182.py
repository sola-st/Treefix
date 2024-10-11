# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
x = array_ops.placeholder(dtypes.float32)
initializer = array_ops.placeholder(dtypes.float32)

def fn(_, current_input):
    exit(current_input)

y = functional_ops.scan(fn, x, initializer=initializer)
self.assertIs(None, y.get_shape().dims)
