# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/grappler_test.py
i = math_ops.cast(x, dtypes.float32)
i = array_ops.reshape(i, [1, 1, 1, 1])
f = math_ops.cast(y, dtypes.float32)
f = array_ops.reshape(f, [1, 1, 1, 1])
c = nn_ops.conv2d(i, f, strides=[1, 1, 1, 1], padding="VALID")
exit(array_ops.reshape(c, ()))
