# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
x_np = [[[[1], [2]], [[3], [4]]]]
block_size = 2
x_out = [[[[1, 2, 3, 4]]]]
for dtype in [
    dtypes.float32, dtypes.float16, dtypes.bfloat16, dtypes.uint8
]:
    self._testOne(x_np, block_size, x_out, dtype=dtype)
