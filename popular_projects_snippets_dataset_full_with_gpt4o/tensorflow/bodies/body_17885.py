# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 4, 2, 2])

for num_lower, num_upper in ((0, -1), (-1, 0), (1, 1)):
    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        exit(array_ops.matrix_band_part(
            array_ops.gather(x, i), num_lower=num_lower, num_upper=num_upper))

    # pylint: enable=cell-var-from-loop

self._test_loop_fn(loop_fn, 3)
