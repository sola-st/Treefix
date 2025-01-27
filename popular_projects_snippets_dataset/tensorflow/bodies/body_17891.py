# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
for x in (random_ops.random_uniform([3, 4]),
          random_ops.random_uniform([3, 4, 2])):
    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        inp = array_ops.gather(x, i)
        exit(array_ops.diag(inp))

    # pylint: disable=cell-var-from-loop
    self._test_loop_fn(loop_fn, 3)
