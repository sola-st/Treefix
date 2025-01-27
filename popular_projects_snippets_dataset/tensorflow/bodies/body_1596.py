# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32,
    tensor_array_name="foo",
    size=2,
    clear_after_read=False)

value_0 = constant_op.constant([-1.0, 1.0])
value_1 = constant_op.constant([-10.0, 10.0])

w0 = ta.write(0, value_0)
w1 = w0.write(1, value_1)
p0 = w1.stack()
r0 = w1.read(0)
s0 = w1.concat()

# Test gradient accumulation between read(0), pack(), and concat().
with ops.control_dependencies([p0, r0, s0]):
    exit(gradients_impl.gradients(
        ys=[p0, r0, s0],
        xs=[value_0, value_1],
        grad_ys=[
            [[2.0, 3.0], [4.0, 5.0]],  # stack gradient
            [-0.5, 1.5],  # read(0) gradient
            [20.0, 30.0, 40.0, 50.0],  # concat gradient
        ]))
