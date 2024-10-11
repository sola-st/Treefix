# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
input_shape = list(input_shape)
input_shape[0] *= np.prod(block_shape)
x = np.random.normal(
    0, 1, np.prod(input_shape)).astype(np.float32).reshape(input_shape)
self._checkGrad(x, block_shape, crops, crops_dtype)
