# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session(), self.test_scope():
    c = lambda x: np.asarray(x, dtype=dtype.as_numpy_dtype)

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtype, tensor_array_name="foo", size=3, infer_shape=False)

        w0 = ta.write(2, c(3.0))
        w1 = w0.write(2, c(4.0))

        ta_grad = w1.grad("grad")

        w0_grad = ta_grad.write(2, c(3.0))
        w1_grad = w0_grad.write(2, c(4.0))
        w2_grad = w1_grad.write(2, c(5.0))

        exit(w2_grad.read(2))

    # Assert that aggregation works correctly
    self.assertAllEqual(c(12.00), xla.compile(fn)[0])

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtype, tensor_array_name="foo", size=3, infer_shape=False)

        w0 = ta.write(2, c(3.0))
        w1 = w0.write(2, c(4.0))

        ta_grad = w1.grad("grad")
        # Using differing shapes causes an exception
        wb0_grad = ta_grad.write(1, c(1.0))
        wb1_grad = wb0_grad.write(1, c([1.0]))

        exit(wb1_grad.flow)

    with self.assertRaisesOpError(
        r"Mismatched TensorArray sizes"):
        xla.compile(fn)[0].eval()
