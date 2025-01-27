# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
# The block size is 0.
x_np = [[[[1], [2]], [[3], [4]]]]
block_size = 0
with self.assertRaises((ValueError, errors.InvalidArgumentError)):
    out_tf = array_ops.space_to_depth(x_np, block_size)
    self.evaluate(out_tf)
