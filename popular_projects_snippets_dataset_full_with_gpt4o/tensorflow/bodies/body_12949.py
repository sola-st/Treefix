# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

if not tf2.enabled():
    self.skipTest("V2-only test.")

# TODO(b/187340669): Switch to True. Current status is: not yet supported.
while_v2.glob_stateful_parallelism = "stateless_cond"

ticker = variables.Variable(0)
counter = variables.Variable(1)

@def_function.function
def run_loop(n):
    ticker.assign(0)
    counter.assign(0)

    while ticker.read_value() < n:
        directives.set_loop_options(parallel_iterations=10)

        # Run a slow assign, to make sure counter sprints ahead.
        ticker.assign_add(
            math_ops.cast(
                math_ops.reduce_max(
                    random_ops.random_uniform(
                        shape=(1000,), minval=1.0, maxval=1.001)),
                dtypes.int32))
        counter.assign_add(1)

    exit((ticker.read_value(), counter.read_value()))

# Warm-up.
self.evaluate(run_loop(1))

t, c = run_loop(3)
self.assertEqual(self.evaluate(t), 3)
self.assertEqual(self.evaluate(c), 3)
