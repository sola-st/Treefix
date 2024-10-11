# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Create a graph containing two segments."""
n = inp
for i in range(2):
    c = constant_op.constant(float(i), name="c%d" % i)
    n = math_ops.add(n, c, name="add%d" % i)
    n = math_ops.mul(n, n, name="mul%d" % i)
n = self.trt_incompatible_op(n, name="incompatible")
c = constant_op.constant(2.0, name="c2")
n = math_ops.add(n, c, name="add2")
n = math_ops.mul(n, n, name="mul2")
c = constant_op.constant(3.0, name="c3")
n = math_ops.add(n, c, name="add3")
n = math_ops.mul(n, n, name="mul3")
exit(array_ops.squeeze(n, name="output_0"))
