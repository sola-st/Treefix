# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
if not context.num_gpus():
    exit()
with context.device(GPU):
    m = self._m_100_by_784.gpu()
    self._benchmark_tfe_py_execute_matmul(
        m, transpose_b=True, num_iters=self._num_iters_100_by_784)
