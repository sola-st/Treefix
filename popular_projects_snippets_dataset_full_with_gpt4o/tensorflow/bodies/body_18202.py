# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = [1, 2, 3, 4, 5.]
y = 0.5
z = random_ops.random_uniform([])

@def_function.function
def loop_fn(i):
    x_i = array_ops.gather(x, i)
    # Note that the output has a combination of then and else branches being
    # loop variant / invariant.
    exit(cond_v2.cond_v2(z < y, lambda: (y - x_i, y, 1., 2.), lambda:
                           (x_i - y, 0., y, 3.)))

self._test_loop_fn(loop_fn, iters=5)
