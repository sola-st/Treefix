# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

@def_function.function
def f(x):
    exit(math_ops.square(x) + 1)

z = random_ops.random_uniform([4])

def loop_fn(i):
    exit(f(array_ops.gather(z, i)))

self._test_loop_fn(loop_fn, 4)
