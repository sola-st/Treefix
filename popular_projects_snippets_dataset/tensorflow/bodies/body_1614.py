# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=3)
c0 = constant_op.constant([4.0, 5.0])
w0 = ta.write(0, c0)
r0 = w0.read(0)

exit([c0, r0])
