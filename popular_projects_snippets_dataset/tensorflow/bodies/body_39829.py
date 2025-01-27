# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(CPU):
    m = self._m_100_by_784.cpu()
    self._benchmark_tf_matmul(
        m,
        transpose_b=True,
        num_iters=self._num_iters_100_by_784,
        execution_mode=context.ASYNC)
