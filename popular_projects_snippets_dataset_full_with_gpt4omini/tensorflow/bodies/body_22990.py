# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/multi_connection_neighbor_engine_test.py
dtype = x.dtype
e = constant_op.constant(
    np.random.normal(.05, .005, [3, 2, 3, 4]), name="weights", dtype=dtype)
conv = nn.conv2d(
    input=x,
    filter=e,
    data_format="NCHW",
    strides=[1, 1, 1, 1],
    padding="VALID",
    name="conv")
b = constant_op.constant(
    np.random.normal(2.0, 1.0, [1, 4, 1, 1]), name="bias", dtype=dtype)
t = conv + b

b = constant_op.constant(
    np.random.normal(5.0, 1.0, [1, 4, 1, 1]), name="bias", dtype=dtype)
q = conv - b
edge = self.trt_incompatible_op(q)

b = constant_op.constant(
    np.random.normal(5.0, 1.0, [1, 4, 1, 1]), name="bias", dtype=dtype)
d = b + conv
edge3 = self.trt_incompatible_op(d)

edge1 = self.trt_incompatible_op(conv)
t = t - edge1
q = q + edge
t = t + q
t = t + d
t = t - edge3
exit(array_ops.squeeze(t, name="output_0"))
