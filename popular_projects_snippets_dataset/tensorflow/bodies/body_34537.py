# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    value = constant_op.constant([[1.0, -1.0], [10.0, -10.0]])

    ta_readonce = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, tensor_array_name="foo", size=2)

    w_readonce = ta_readonce.unstack(value)
    r0_readonce = w_readonce.read(0)

    with self.assertRaisesOpError(
        r"Could not read index 0 twice because it was cleared after a "
        r"previous read \(perhaps try setting clear_after_read = false\?\)"):
        with ops.control_dependencies([r0_readonce]):
            self.evaluate(w_readonce.read(0))

    ta_readtwice = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=2,
        clear_after_read=False)
    w_readtwice = ta_readtwice.unstack(value)
    r0_readtwice = w_readtwice.read(0)
    with ops.control_dependencies([r0_readtwice]):
        r1_readtwice = w_readtwice.read(0)

    self.assertAllEqual([1.0, -1.0], self.evaluate(r1_readtwice))
