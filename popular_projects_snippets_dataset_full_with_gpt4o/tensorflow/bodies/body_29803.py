# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
x_np = [[[[1, 2, 3, 4],
          [5, 6, 7, 8]],
         [[9, 10, 11, 12],
          [13, 14, 15, 16]]]]
block_size = 4
# Raise an exception, since th depth is only 4 and needs to be
# divisible by 16.
with self.assertRaises(ValueError):
    out_tf = array_ops.depth_to_space(x_np, block_size)
    self.evaluate(out_tf)
