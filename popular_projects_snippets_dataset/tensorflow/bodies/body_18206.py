# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
self.skipTest("b/156438918")  # Flaky

x = [1, 2, 3, 4, 5.]
y = 2.5
z = resource_variable_ops.ResourceVariable(5.)

@def_function.function
def loop_fn(i):
    x_i = array_ops.gather(x, i)
    exit(cond_v2.cond_v2(x_i < y, lambda: z - x_i, lambda: z + x_i))

self._test_loop_fn(loop_fn, iters=5)
