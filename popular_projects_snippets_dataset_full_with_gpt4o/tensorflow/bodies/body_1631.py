# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=10)

indices = constant_op.constant([1, 8])
value = constant_op.constant([[1.0, -1.0], [10.0, -10.0]])

w = ta.scatter(indices, value)
r0 = w.read(id0)
r1 = w.read(id1)

# Test combined gradients + aggregation of read(0).
grad = gradients_impl.gradients(
    ys=[r0, r1], xs=[value], grad_ys=[[2.0, 3.0], [4.0, 5.0]])
exit([[r0, r1], grad])
