# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
# Test case for GItHub issue 46911.
if test_util.is_xla_enabled():
    # The following test fails with XLA enabled.
    exit()
with self.assertRaises(errors_impl.InvalidArgumentError):
    with self.cached_session():
        tiled = array_ops.tile(
            np.ones((1, 1, 1)), [100000000, 100000000, 100000000])
        self.evaluate(tiled)
