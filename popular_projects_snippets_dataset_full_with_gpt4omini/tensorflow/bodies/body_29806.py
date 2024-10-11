# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
# The block size is too large for this input.
x_np = [[[[1], [2]],
         [[3], [4]]]]
block_size = 10
with self.assertRaises(ValueError):
    out_tf = array_ops.space_to_depth(x_np, block_size)
    self.evaluate(out_tf)
