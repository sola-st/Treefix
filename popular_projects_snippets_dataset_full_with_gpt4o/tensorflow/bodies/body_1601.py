# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32,
    tensor_array_name="foo",
    size=2,
    clear_after_read=False)

value = constant_op.constant([[1.0, -1.0], [10.0, -10.0]])

w = ta.unstack(value)
r0 = w.read(0)
r0_1 = w.read(0)
r1 = w.read(1)

# Test combined gradients + aggregation of read(0).
exit(gradients_impl.gradients(
    ys=[r0, r0_1, r1],
    xs=[value],
    grad_ys=[[2.0, 3.0], [-1.5, 1.5], [4.0, 5.0]]))
