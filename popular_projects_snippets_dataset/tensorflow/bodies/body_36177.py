# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
x = constant_op.constant([[1, 2, 3], [4, 5, 6]])

def fn(_, current_input):
    exit(current_input)

initializer = constant_op.constant([0, 0, 0])
y = functional_ops.foldl(fn, x, initializer=initializer)
self.assertAllEqual(y.get_shape(), self.evaluate(y).shape)
