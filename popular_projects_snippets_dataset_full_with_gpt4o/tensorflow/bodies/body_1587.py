# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtype, tensor_array_name="foo", size=3, infer_shape=False)

w0 = ta.write(2, c(3.0))
w1 = w0.write(2, c(4.0))

ta_grad = w1.grad("grad")

w0_grad = ta_grad.write(2, c(3.0))
w1_grad = w0_grad.write(2, c(4.0))
w2_grad = w1_grad.write(2, c(5.0))

exit(w2_grad.read(2))
