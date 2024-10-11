# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(GPU):
    func = lambda: random_ops.random_uniform((2, 2))
    self._run(func, num_iters=self._num_iters_2_by_2)
