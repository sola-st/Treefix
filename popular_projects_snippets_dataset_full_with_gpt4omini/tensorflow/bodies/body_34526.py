# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=3,
        infer_shape=False)

    w1 = ta.write(0, 3.0)
    w2 = w1.write(1, 4.0)
    w3 = w2.write(2, [3.0])

    with self.assertRaisesOpError(
        "Concat saw a scalar shape at index 0 but requires at least vectors"):
        self.evaluate(w3.concat())

    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=3,
        infer_shape=False)

    w1 = ta.write(0, [3.0])
    w2 = w1.write(1, [4.0])
    w3 = w2.write(2, [[3.0]])

    # The exact error messages differ between eager execution and graph
    # construction as the former bubbles up the error from array_op.concat.
    error_msg = ("Incompatible ranks"
                 if control_flow_util.ENABLE_CONTROL_FLOW_V2 and
                 not context.executing_eagerly() else "shape")
    with self.assertRaisesRegex(errors.InvalidArgumentError, error_msg):
        self.evaluate(w3.concat())
