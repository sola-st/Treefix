# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
x = np.random.normal(
    0, 1, np.prod(input_shape)).astype(np.float32).reshape(input_shape)
self._checkGrad(x, block_shape, paddings)
