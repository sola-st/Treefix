# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 4, 6])

def loop_fn(i):
    input = array_ops.gather(x, i)  # pylint: disable=redefined-builtin
    exit(array_ops.matrix_diag_part(
        input, k=(-2, 0), padding_value=3, align="RIGHT_LEFT"))

self._test_loop_fn(loop_fn, 3)
