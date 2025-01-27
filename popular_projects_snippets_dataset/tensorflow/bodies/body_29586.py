# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
block_size_sq = block_size * block_size
x = np.random.normal(0, 1, b * h * w * d *
                     block_size_sq).astype(np.float32).reshape(
                         [b, h * block_size, w * block_size, d])
paddings = np.array(
    [[pad_beg, pad_end], [pad_beg, pad_end]], dtype=np.int32)

self._checkGrad(x, paddings, block_size)
