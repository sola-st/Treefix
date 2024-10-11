# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Create a graph containing multiple segments."""
c1 = constant_op.constant(1.0, name="c1")
c2 = constant_op.constant(2.0, name="c2")
d1 = self.trt_incompatible_op(inp, name="d1")
d2 = self.trt_incompatible_binary_op(inp, inp, name="d2")
with ops.control_dependencies([d1]):
    add = math_ops.add(inp, c1, name="add")
mul = math_ops.mul(add, add, name="mul")
add1 = math_ops.add(mul, mul, name="add1")
edge = self.trt_incompatible_op(add1, name="incompatible")
with ops.control_dependencies([d1, d2, add1]):
    add2 = math_ops.add(edge, c2, name="add2")
mul1 = math_ops.mul(add2, add2, name="mul1")
add3 = math_ops.add(mul1, mul1, name="add3")
inc1 = self.trt_incompatible_binary_op(d1, add3, name="incompatible1")
inc2 = self.trt_incompatible_binary_op(d2, inc1, name="incompatible2")
exit(array_ops.squeeze(inc2, name="output_0"))
