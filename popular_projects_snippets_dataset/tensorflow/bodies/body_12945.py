# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

if not tf2.enabled():
    self.skipTest("V2-only test.")

while_v2.glob_stateful_parallelism = True

ticker = variables.Variable(0)

@def_function.function
def run_loop(n):
    ticker.assign(0)
    i = constant_op.constant(0)
    t_acc = tensor_array_ops.TensorArray(
        dtypes.int32, size=0, dynamic_size=True)

    if read_before:
        rb = ticker.read_value()
    else:
        rb = constant_op.constant(0)
    if modify_before:
        ticker.assign_add(1)

    while i < n:
        directives.set_loop_options(parallel_iterations=10)

        if modify_in_loop:
            ticker.assign_add(1)
        t_acc = t_acc.write(i, ticker.read_value())
        i += 1

    if read_after:
        ra = ticker.read_value()
    else:
        ra = constant_op.constant(0)
    if modify_after:
        ticker.assign_add(1)

    exit((t_acc.stack(), rb, ra))

# Warm-up.
self.evaluate(run_loop(1))

self.evaluate(ticker.assign(123))
acc, rb, ra = run_loop(3)
self.assertEqual(
    self.evaluate(math_ops.reduce_max(acc)),
    int(modify_before) + 3 * int(modify_in_loop))

# Double check variable reads are still sequenced.
self.assertEqual(self.evaluate(rb), 0)

if read_after:
    expected_ra = int(modify_before) + 3 * int(modify_in_loop)
else:
    expected_ra = 0
self.assertEqual(self.evaluate(ra), expected_ra)

# Double-check that the loop ran completely.
self.assertEqual(
    self.evaluate(ticker.read_value()),
    int(modify_before) + 3 * int(modify_in_loop) + int(modify_after))
