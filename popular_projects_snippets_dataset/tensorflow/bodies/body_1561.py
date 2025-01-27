# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=tf_dtype, tensor_array_name="foo", size=3)

# Unpack a matrix into vectors.
w1 = ta.unstack(
    convert([[1.0, 1.03125], [2.0, 2.03125], [3.0, 3.03125]]))
r0 = w1.read(0)
r1 = w1.read(1)
r2 = w1.read(2)
exit([r0, r1, r2])
