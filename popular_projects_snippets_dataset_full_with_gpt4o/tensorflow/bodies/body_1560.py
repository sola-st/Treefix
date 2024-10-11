# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=tf_dtype, tensor_array_name="foo", size=3)

# Unpack a vector into scalars
w0 = ta.unstack(convert([1.0, 2.0, 3.0]))
r0 = w0.read(0)
r1 = w0.read(1)
r2 = w0.read(2)

exit([r0, r1, r2])
