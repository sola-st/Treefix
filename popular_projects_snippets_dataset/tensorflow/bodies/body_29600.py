# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
data = np.random.randn(*shape)
if dtype == np.bool_:
    exit(data < 0)  # Naive casting yields True with P(1)!
else:
    exit(data.astype(dtype))
