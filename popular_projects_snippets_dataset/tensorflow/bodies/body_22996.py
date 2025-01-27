# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Create a graph containing multiple segment."""
dtype = inp.dtype
conv_filter = constant_op.constant(
    [[[[1., 0.5, 4., 6., 0.5, 1.], [1., 0.5, 1., 1., 0.5, 1.]]]],
    name="weights",
    dtype=dtype)
conv = nn.conv2d(
    input=inp,
    filter=conv_filter,
    strides=[1, 2, 2, 1],
    padding="SAME",
    name="conv")
c1 = constant_op.constant(
    np.random.randn(12, 12, 6), dtype=dtype, name="c1")
p = math_ops.mul(conv, c1, name="mul")
c2 = constant_op.constant(
    np.random.randn(12, 12, 6), dtype=dtype, name="c2")
q = math_ops.div(conv, c2, name="div")

edge = self.trt_incompatible_op(q, name="incompatible")
one = constant_op.constant(1, name="one", dtype=dtype)
edge = math_ops.sub(one, edge, name="one_sub")
edge = math_ops.div(edge, edge, name="div1")
r = math_ops.add(edge, edge, name="add")

p = math_ops.sub(p, edge, name="sub")
q = math_ops.mul(q, edge, name="mul1")
s = math_ops.add(p, q, name="add1")
s = math_ops.sub(s, r, name="sub1")
exit(array_ops.squeeze(s, name="output_0"))
