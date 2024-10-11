# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/save_restore_ops_test.py
with ops.Graph().as_default():
    op = io_ops.restore_v2("model", ["var1", "var2"], ["", "3 4 0,1:-"],
                           [dtypes.float32, dtypes.float32])
    self.assertEqual(2, len(op))
    self.assertFalse(op[0].get_shape().is_fully_defined())
    self.assertEqual([1, 4], op[1].get_shape())
