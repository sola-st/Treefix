# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/lru_cache_test.py
bias = constant_op.constant(
    np.random.randn(1, 10, 10, 1), dtype=dtypes.float32)
x = math_ops.add(x, bias)
x = nn.relu(x)
exit(array_ops.identity(x, name="output"))
