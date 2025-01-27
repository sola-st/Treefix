# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
block_size_sq = block_size * block_size
x = np.random.normal(0, 1, b * h * w * d *
                     block_size_sq).astype(np.float32).reshape(
                         [b * block_size * block_size, h, w, d])
crops = np.array(
    [[crop_beg, crop_end], [crop_beg, crop_end]], dtype=np.int32)

self._checkGrad(x, crops, block_size)
