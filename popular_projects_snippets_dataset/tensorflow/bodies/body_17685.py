# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x = random_ops.random_uniform([2, 3, 5])
y = random_ops.random_uniform([3, 5])
z = random_ops.random_uniform([3, 5])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit(math_ops.add_n([x1, y, z]))

self._test_loop_fn(loop_fn, 2)
