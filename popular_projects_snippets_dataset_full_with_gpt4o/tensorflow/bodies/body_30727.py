# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
a = variables.Variable(constant_op.constant(1.0, shape=[1]))
b = variables.Variable(constant_op.constant(2.0, shape=[1]))
with self.assertRaises(ValueError):
    array_ops.concat(b, a)
with self.assertRaises(TypeError):
    array_ops.concat(1, 4.2)
with self.assertRaises(ValueError):
    array_ops.concat(1, a)
with self.assertRaises(TypeError):
    array_ops.concat([a, b], a)
with self.assertRaises(ValueError):
    array_ops.concat([a, b], [3])
with self.assertRaises(ValueError):
    array_ops.concat([], 0)
# An integer tensor for shape dim should throw no error.
array_ops.concat(1, constant_op.constant(0, shape=[]))
# A non-scalar tensor for shape should throw ValueError.
with self.assertRaises(ValueError):
    array_ops.concat(1, constant_op.constant(0, shape=[1]))
