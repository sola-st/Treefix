# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/save_restore_ops_test.py
os.chdir(self.get_temp_dir())
self.evaluate(io_ops.save_v2(
    "ckpt", ["x"], [""], [constant_op.constant(100.)]))
self.assertAllEqual([100.],
                    self.evaluate(io_ops.restore_v2(
                        "ckpt", ["x"], [""], [dtypes.float32])))
