# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=0,
        dynamic_size=True,
        infer_shape=True)
    value = constant_op.constant([[1.0, -1.0], [2.0, -2.0], [3.0, -3.0]])
    w0 = ta.split(value, [1, 1, 1])
    r0 = w0.read(0)
    self.assertAllEqual((1, 2), r0.get_shape())

    ta1 = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo1",
        size=0,
        dynamic_size=True,
        infer_shape=True)
    w0 = ta1.split(value, [1, 2])
    r0 = w0.read(0)
    if context.executing_eagerly():
        self.assertEqual((1, 2), r0.get_shape())
        self.assertEqual((2, 2), w0.read(1).get_shape())
    else:
        self.assertEqual(r0.get_shape().ndims, None)
        if not control_flow_util.ENABLE_CONTROL_FLOW_V2:
            self.assertEqual(
                tensor_shape.TensorShape(
                    ta1.handle.op.get_attr("element_shape")).ndims, None)
