# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(device):

    def func():
        exit(random_ops.random_uniform(shape, maxval=3, dtype=dtype))

    self._run(func, num_iters=self._num_iters_2_by_2)
