# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
# The block size is too large for this input.
x_np = [[[[1], [2]], [[3], [4]]]]
crops = np.zeros((2, 2), dtype=np.int32)
block_size = 10
with self.assertRaises(ValueError):
    out_tf = self.batch_to_space(x_np, crops, block_size)
    self.evaluate(out_tf)
