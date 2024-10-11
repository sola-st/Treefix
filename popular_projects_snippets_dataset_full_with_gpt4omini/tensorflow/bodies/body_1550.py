# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=3)

w0 = ta.write(0, [[4.0, 5.0]])
w1 = w0.write(1, [[1.0, 3.0]])
w2 = w1.write(2, [[7.0, -8.5]])

r0 = w2.read(0)
r1 = w2.read(1)
r2 = w2.read(2)
flow = w2.flow
exit([r0, r1, r2, flow])
