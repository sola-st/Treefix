# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pool_test.py
# Use negative numbers to make sure there isn't any zero padding getting
# used.
x = -np.arange(
    np.prod(input_shape), dtype=np.float32).reshape(input_shape) - 1
y1 = pool_direct(input=x, **kwargs)
y2 = nn_ops.pool(input=x, **kwargs)
self.assertAllClose(y1, self.evaluate(y2), rtol=1e-2, atol=1e-2)
