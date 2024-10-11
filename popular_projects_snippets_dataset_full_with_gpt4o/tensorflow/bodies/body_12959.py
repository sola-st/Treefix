# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
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
