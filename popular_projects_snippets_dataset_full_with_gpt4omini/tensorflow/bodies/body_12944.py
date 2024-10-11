# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
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
