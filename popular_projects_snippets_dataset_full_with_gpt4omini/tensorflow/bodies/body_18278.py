# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

z = random_ops.random_uniform([4, 2])
v = variables.Variable(z[0])

@def_function.function
def f(x):
    exit(math_ops.square(x) + v + 1)

def loop_fn(i):
    z_i = array_ops.gather(z, i)
    with backprop.GradientTape() as g:
        g.watch(z_i)
        out = f(z_i)
    exit((out, g.gradient(out, z_i)))

self._test_loop_fn(loop_fn, 4)
