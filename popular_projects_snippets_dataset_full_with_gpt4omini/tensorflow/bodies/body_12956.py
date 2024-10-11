# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

while_v2.glob_stateful_parallelism = True

@def_function.function
def run_loop(n):

    a = 0
    b = 1

    i = constant_op.constant(0)
    while i < n:
        directives.set_loop_options(parallel_iterations=10)
        i += 1
        a += 2
        b *= 3

    exit((i, a, b))

i, a, b = run_loop(3)
self.assertEqual(self.evaluate(i), 3)
self.assertEqual(self.evaluate(a), 6)
self.assertEqual(self.evaluate(b), 27)
