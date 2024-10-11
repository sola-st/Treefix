# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/save_restore_ops_test.py
with ops.Graph().as_default():
    with self.assertRaises(ValueError):
        io_ops.restore_v2("model", ["var1", "var2", "var3"], ["", "3 4 0,1:-"],
                          [dtypes.float32, dtypes.float32])
