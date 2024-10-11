# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
# The input is missing the last dimension ("depth")
x_np = [[[1, 2], [3, 4]]]
block_size = 2
with self.assertRaises((ValueError, errors.InvalidArgumentError)):
    out_tf = array_ops.space_to_depth(x_np, block_size)
    self.evaluate(out_tf)
