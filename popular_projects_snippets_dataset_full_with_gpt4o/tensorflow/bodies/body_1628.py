# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=tf_dtype, tensor_array_name="foo", size=10)

indices = constant_op.constant([1, 8])
value = constant_op.constant(convert([[1.0, 5.0], [10.0, 20.0]]))

w = ta.scatter(indices, value)
r0 = w.read(id0)
r1 = w.read(id1)

exit([r0, r1])
