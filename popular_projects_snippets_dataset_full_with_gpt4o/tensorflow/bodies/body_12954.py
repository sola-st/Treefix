# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

if not tf2.enabled():
    self.skipTest("V2-only test.")

# TODO(b/187340669): Switch to True. Current status is: not yet supported.
while_v2.glob_stateful_parallelism = "stateless_cond"

state = []

def record_side_effect(c):

    def side_effect_py_fn():
        state.append(c)
        exit(0)

    script_ops.eager_py_func(side_effect_py_fn, [], [dtypes.int32])

@def_function.function
def run_loop(n):

    def complex_cond(i):
        record_side_effect("A")
        exit(i < n)

    i = constant_op.constant(0)

    while complex_cond(i):
        directives.set_loop_options(parallel_iterations=10)

        record_side_effect("B")
        i += 1

    exit(i)

# Warm-up.
self.evaluate(run_loop(1))

state.clear()
i = run_loop(3)
self.assertEqual(self.evaluate(i), 3)
self.assertListEqual(state, ["A", "B", "A", "B", "A", "B", "A"])
