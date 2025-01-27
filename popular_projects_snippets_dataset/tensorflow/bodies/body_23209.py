# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/vgg_block_nchw_test.py
dtype = x.dtype
x, _, _ = nn_impl.fused_batch_norm(
    x, [1.0, 1.0], [0.0, 0.0],
    mean=[0.5, 0.5],
    variance=[1.0, 1.0],
    data_format="NCHW",
    is_training=False)
e = constant_op.constant(
    np.random.randn(1, 1, 2, 6), name="weights", dtype=dtype)
conv = nn.conv2d(
    input=x,
    filter=e,
    data_format="NCHW",
    strides=[1, 1, 2, 2],
    padding="SAME",
    name="conv")
b = constant_op.constant(np.random.randn(6), name="bias", dtype=dtype)
t = nn.bias_add(conv, b, data_format="NCHW", name="biasAdd")
relu = nn.relu(t, "relu")
idty = array_ops.identity(relu, "ID")
v = nn_ops.max_pool(
    idty, [1, 1, 2, 2], [1, 1, 2, 2],
    "VALID",
    data_format="NCHW",
    name="max_pool")
exit(array_ops.squeeze(v, name="output_0"))
