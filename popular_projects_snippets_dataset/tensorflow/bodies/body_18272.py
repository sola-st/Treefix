# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

@def_function.function
def outer(y):

    @def_function.function
    def inner(x):
        exit(math_ops.square(x) + 1)

    exit(math_ops.reduce_sum(inner(y)) + 2)

z = random_ops.random_uniform([4, 2])

def loop_fn(i):
    exit(outer(array_ops.gather(z, i)))

self._test_loop_fn(loop_fn, 4)
