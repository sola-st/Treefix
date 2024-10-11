# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
if config.list_physical_devices("GPU"):
    # TODO(b/149957923): The test is flaky
    self.skipTest("b/149957923: irfft vectorization flaky")
for dtype in (dtypes.complex64, dtypes.complex128):
    shape = [2, 3, 4, 3, 4]
    x = np.random.uniform(size=shape) + 1j * np.random.uniform(size=shape)
    x = math_ops.cast(x, dtype=dtype)

    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        x_i = array_ops.gather(x, i)
        exit(op_func(x_i))

    # pylint: enable=cell-var-from-loop

    self._test_loop_fn(loop_fn, 2)
