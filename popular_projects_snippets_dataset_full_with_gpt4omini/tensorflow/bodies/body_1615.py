# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=3)
c1 = constant_op.constant([6.0, 7.0])
w0 = ta.write(0, c0)
w1 = w0.write(1, c1)
r0 = w1.read(0)
r1 = w1.read(1)

exit([r0, c1, r1])
