# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with context.eager_mode():

    def _test(x, y, device):
        self.assertAllEqual(x.numpy(), y.numpy())
        self.assertTrue(device in y.device.lower())

    with test_util.force_gpu():
        a = constant_op.constant([[2], [3]], dtype=dtypes.float32)
    with test_util.force_gpu():
        b = array_ops.identity(a)
        _test(a, b, "gpu")
    with test_util.force_cpu():
        c = array_ops.identity(b)
        _test(b, c, "cpu")
    with test_util.force_cpu():
        d = array_ops.identity(c)
        _test(c, d, "cpu")
    with test_util.force_gpu():
        e = array_ops.identity(d)
        _test(d, e, "gpu")
