# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/save_restore_ops_test.py
with ops.Graph().as_default():
    op = gen_io_ops.restore_slice("model", "var", "3 4 0,1:-", dtypes.float32)
    self.assertEqual([1, 4], op.get_shape())
