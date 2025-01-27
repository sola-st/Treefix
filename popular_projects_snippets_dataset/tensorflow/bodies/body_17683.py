# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
a = random_ops.random_uniform([3, 5])

def loop_fn(i):
    x1 = array_ops.gather(a, i)
    with framework_ops.colocate_with(x1):
        exit(x1 * 2)

self._test_loop_fn(loop_fn, 3)
