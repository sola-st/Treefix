# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Create a graph containing single segment."""
n = inp
c = constant_op.constant(1.0, name="c")
n = math_ops.add(n, c, name="add")
n = math_ops.mul(n, n, name="mul")
n = math_ops.add(n, n, name="add1")
exit(array_ops.squeeze(n, name="output_0"))
