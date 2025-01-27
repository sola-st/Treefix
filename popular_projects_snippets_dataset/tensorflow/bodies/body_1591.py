# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
h1 = tensor_array_ops.TensorArray(
    size=1, dtype=dtypes.float32, tensor_array_name="foo")
w1 = h1.write(0, 4.0)
r1 = w1.read(0)

h2 = tensor_array_ops.TensorArray(
    size=1, dtype=dtypes.float32, tensor_array_name="bar")

w2 = h2.write(0, 5.0)
r2 = w2.read(0)
exit(r1 + r2)
