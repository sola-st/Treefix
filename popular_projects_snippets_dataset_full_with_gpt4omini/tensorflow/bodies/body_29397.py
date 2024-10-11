# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
block_size_sq = block_size * block_size
data = np.random.normal(0, 1, b * h * w * d * block_size_sq).astype(
    np.float32)
if data_format == "NHWC":
    x = data.reshape([b, h * block_size, w * block_size, d])
else:
    x = data.reshape([b, d, h * block_size, w * block_size])

self._checkGrad(x, block_size, data_format)
