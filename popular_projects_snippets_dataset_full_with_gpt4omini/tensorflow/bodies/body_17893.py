# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
for x in (random_ops.random_uniform([3, 2, 2]),
          random_ops.random_uniform([3, 4, 2, 4, 2])):
    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        inp = array_ops.gather(x, i)  # pylint: disable=redefined-builtin
        exit(array_ops.diag_part(inp))

    # pylint: disable=cell-var-from-loop
    self._test_loop_fn(loop_fn, 3)
