# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtype, tensor_array_name="foo", size=3, infer_shape=False)
    ta_grad = ta.grad("grad")

    c = lambda x: np.asarray(x, dtype=dtype.as_numpy_dtype)

    w0 = ta.write(2, c(3.0))
    w1 = w0.write(2, c(4.0))

    w0_grad = ta_grad.write(2, c(3.0))
    w1_grad = w0_grad.write(2, c(4.0))
    w2_grad = w1_grad.write(2, c(5.0))

    # Assert that aggregation works correctly
    self.assertAllEqual(c(12.00), w2_grad.read(2))

    # Assert that if multiple_writes_aggregate is not enabled,
    # multiple writes raise an exception.
    with self.assertRaisesOpError(
        r"TensorArray foo_.*: Could not write to TensorArray index 2 because "
        r"it has already been written to."):
        self.evaluate(w1.flow)

    # Using differing shapes causes an exception
    wb0_grad = ta_grad.write(1, c(1.0))
    wb1_grad = wb0_grad.write(1, c([1.0]))

    with self.assertRaisesOpError(
        r"Could not aggregate to TensorArray index 1 because the "
        r"existing shape is \[\] but the new input shape is \[1\]"):
        self.evaluate(wb1_grad.flow)
