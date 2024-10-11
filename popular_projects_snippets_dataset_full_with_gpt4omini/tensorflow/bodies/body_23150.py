# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/memory_alignment_test.py
dtype = inp.dtype
e1 = constant_op.constant(
    np.random.randn(1, 1, 3, 5), name="kernel_1", dtype=dtype)
e2 = constant_op.constant(
    np.random.randn(1, 1, 5, 10), name="kernel_2", dtype=dtype)
conv = nn.conv2d(
    input=inp,
    filter=e1,
    strides=[1, 1, 1, 1],
    padding="VALID",
    name="conv")
out = nn.conv2d(
    input=conv,
    filter=e2,
    strides=[1, 1, 1, 1],
    padding="VALID",
    name="conv_2")
exit(array_ops.squeeze(out, name="output_0"))
