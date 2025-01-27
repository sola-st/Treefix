# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=tf_dtype, tensor_array_name="foo", size=3)

w0 = ta.write(0, convert([[4.0, 5.0]]))
w1 = w0.write(1, convert([[6.0, 7.0]]))
w2 = w1.write(2, convert([[8.0, 9.0]]))

exit(w2.stack())
