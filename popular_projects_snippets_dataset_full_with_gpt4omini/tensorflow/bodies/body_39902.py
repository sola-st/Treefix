# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
if is_rate_tensor:
    rate = constant_op.constant(rate, dtype=dtypes.float32)
with context.device(device):

    def func():
        exit(nn_ops.dropout(
            self._m_2_by_2, rate=rate, noise_shape=noise_shape))

    self._run(func, num_iters=self._num_iters_2_by_2)
