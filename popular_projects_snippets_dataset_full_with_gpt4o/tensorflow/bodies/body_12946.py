# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
ticker.assign(0)
i = constant_op.constant(0)
t_acc = tensor_array_ops.TensorArray(
    dtypes.int32, size=0, dynamic_size=True)

while i < n:
    directives.set_loop_options(parallel_iterations=10)

    a = ticker.read_value()
    b = ticker.read_value()
    t_acc = t_acc.write(2 * i, a)
    t_acc = t_acc.write(2 * i + 1, b)

    # Slow write forces reads to sprint ahead if they can.
    # This test verifies that they don't.
    ticker.assign_add(
        math_ops.cast(
            math_ops.reduce_max(
                random_ops.random_uniform(
                    shape=(1000,), minval=1.0, maxval=1.001)),
            dtypes.int32))

    i += 1

a = ticker.read_value()
b = ticker.read_value()
t_acc = t_acc.write(2 * i, a)
t_acc = t_acc.write(2 * i + 1, b)

exit(t_acc.stack())
