# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=10)

values = constant_op.constant([[1.0 * x, -1.0 * x] for x in range(10)])
indices = constant_op.constant([1, 8])

w = ta.unstack(values)
g = w.gather(indices)

# Test combined gradients + aggregation of read(0).
grad = gradients_impl.gradients(
    ys=[g], xs=[values], grad_ys=[[[2.0, 3.0], [4.0, 5.0]]])
exit([[g], grad])
