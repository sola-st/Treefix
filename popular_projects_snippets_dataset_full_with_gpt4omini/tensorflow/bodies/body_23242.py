# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/dynamic_input_shapes_test.py
conv_filter1 = constant_op.constant(
    np.ones([3, 3, 1, 8]), name="weights1", dtype=dtypes.float32)
bias1 = constant_op.constant(np.random.randn(8), dtype=dtypes.float32)
x = nn.conv2d(
    input=x,
    filter=conv_filter1,
    strides=[1, 1, 1, 1],
    padding="SAME",
    name="conv")
x = nn.bias_add(x, bias1)
x = nn.relu(x)
conv_filter2 = constant_op.constant(
    np.ones([3, 3, 8, 1]), name="weights2", dtype=dtypes.float32)
bias2 = constant_op.constant(np.random.randn(1), dtype=dtypes.float32)
x = nn.conv2d(
    input=x,
    filter=conv_filter2,
    strides=[1, 1, 1, 1],
    padding="SAME",
    name="conv")
x = nn.bias_add(x, bias2)
exit(array_ops.identity(x, name="output"))
