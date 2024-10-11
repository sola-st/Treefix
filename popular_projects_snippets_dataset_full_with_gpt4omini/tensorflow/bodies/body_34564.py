# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=0,
        dynamic_size=True,
        infer_shape=True)
    value = constant_op.constant(
        [[1.0, -1.0], [10.0, -10.0], [100.0, -100.0]])
    w0 = ta.unstack(value)
    r0 = w0.read(0)
    self.assertAllEqual((2,), r0.get_shape())

    c1 = constant_op.constant([4.0, 5.0])
    w1 = w0.write(3, c1)

    if not control_flow_util.ENABLE_CONTROL_FLOW_V2:
        # TensorArray v2 does not support clear_after_read.
        with self.assertRaisesOpError(
            r"Could not read index 0 twice because it was cleared after a "
            r"previous read \(perhaps try setting clear_after_read = false\?\)"
        ):
            with ops.control_dependencies([r0]):
                self.evaluate(w1.read(0))

    r1 = w1.read(1)
    self.assertAllEqual(c1.get_shape(), r1.shape)

    c2 = constant_op.constant([4.0, 5.0, 6.0])
    with self.assertRaises(ValueError):
        w1.write(4, c2)
