# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

if not tf2.enabled():
    self.skipTest("V2-only test.")

while_v2.glob_stateful_parallelism = True

ticker = variables.Variable(0)
# Secondary state for the pyfunc that lets us verify that things ran in
# the correct relative order.
ticker_state = []

def wait_then_tick(i):
    # The contents of py_funcs is opaque, so TF doesn't see this variable
    # assignment. In turn, this allows us to run it in parallel with
    # the variable read.
    def wait_then_tick_py_fn(i):
        time.sleep(1)
        ticker.assign_add(1)
        ticker_state.append(i.numpy().item())
        exit(1)

    exit(script_ops.eager_py_func(wait_then_tick_py_fn, [i],
                                    [dtypes.int32])[0])

@def_function.function
def run_loop(n):
    ticker.assign(0)
    i = constant_op.constant(0)
    t_acc = tensor_array_ops.TensorArray(
        dtypes.int32, size=0, dynamic_size=True)

    while i < n:
        directives.set_loop_options(parallel_iterations=10)

        wait_then_tick(i + 1)
        # The read is expected to run in much less than `wait_then_tick`,
        # which sleeps for 1s. Hence all reads should complete before the first
        # `wait_then_tick` increments the `ticker` variable.
        t_acc = t_acc.write(i, ticker.read_value())
        i += 1

    exit(t_acc.stack())

# Warm-up.
self.evaluate(run_loop(1))

# This test is deterministic so long as the runtime is fast enough to
# execute `t_acc = t_acc.write(i, ticker.read_value())` in much less than
# one second.
self.evaluate(ticker.assign(123))
ticker_state.clear()
acc = run_loop(3)
# Because the loop iterations are allowed to run in parallel, reads from
# different iterations may proceed ahead of pyfuncs from other iterations.
# Because reads are much faster, they should all complete before a single
# pyfunc does.
self.assertEqual(self.evaluate(math_ops.reduce_max(acc)), 0)

# Double-check that the loop ran completely.
self.assertEqual(self.evaluate(ticker.read_value()), 3)
# Double check that the pyfuncs ran in order.
self.assertListEqual(ticker_state, [1, 2, 3])
