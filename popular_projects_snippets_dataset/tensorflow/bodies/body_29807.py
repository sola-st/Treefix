# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
# The depth is not divisible by the square of the block size.
x_np = [[[[1, 1, 1, 1],
          [2, 2, 2, 2]],
         [[3, 3, 3, 3],
          [4, 4, 4, 4]]]]
block_size = 3
with self.assertRaises(ValueError):
    _ = array_ops.space_to_depth(x_np, block_size)
