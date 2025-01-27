# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_function_test.py
dtype = inp.dtype
conv_filter = constant_op.constant([[[[1., 0.5, 4.], [1., 0.5, 1.]]]],
                                   name="weights",
                                   dtype=dtype)
conv = nn.conv2d(
    input=inp,
    filter=conv_filter,
    strides=[1, 2, 2, 1],
    padding="SAME",
    name="conv")
bias = constant_op.constant([4., 1.5, 2.], name="bias", dtype=dtype)
added = nn.bias_add(conv, bias, name="bias_add")
relu = nn.relu(added, "relu")
identity = array_ops.identity(relu, "identity")
pool = nn_ops.max_pool(
    identity, [1, 2, 2, 1], [1, 2, 2, 1], "VALID", name="max_pool")
exit(array_ops.squeeze(pool))
