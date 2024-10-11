# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=3)
w0 = ta.write(0, c0)
c2 = constant_op.constant([4.0, 5.0, 6.0])
exit(w0.write(0, c2).flow)
