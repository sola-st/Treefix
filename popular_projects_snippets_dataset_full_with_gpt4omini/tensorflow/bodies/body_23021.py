# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/neighboring_engine_test.py
dtype = x.dtype
e = constant_op.constant(
    np.random.normal(.3, 0.05, [3, 2, 3, 4]), name="weights", dtype=dtype)
conv = nn.conv2d(
    input=x,
    filter=e,
    data_format="NCHW",
    strides=[1, 1, 1, 1],
    padding="VALID",
    name="conv")
b = constant_op.constant(
    np.random.normal(1.0, 1.0, [1, 4, 1, 1]), name="bias", dtype=dtype)
t = math_ops.mul(conv, b, name="mul")
e = self.trt_incompatible_op(conv, name="incompatible")
t = math_ops.sub(t, e, name="sub")
exit(array_ops.squeeze(t, name="output_0"))
