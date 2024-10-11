# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
x_np = [[[[1, 1, 1, 1],
          [2, 2, 2, 2]],
         [[3, 3, 3, 3],
          [4, 4, 4, 4]]]]
block_size = 1
with self.assertRaises(ValueError):
    out_tf = array_ops.depth_to_space(x_np, block_size)
    self.evaluate(out_tf)
