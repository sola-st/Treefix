# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session() as sess:
    ta = tensor_array_ops.TensorArray(
        size=3, dtype=dtypes.float32,
        element_shape=None)  # Note that element_shape is unknown
    handle, flow = data_flow_ops.tensor_array_grad_with_shape(
        handle=ta.handle,
        flow_in=ta.flow,
        shape_to_prepend=tensor_shape.TensorShape([4, 5]),
        source="source")
    ta_grad = tensor_array_ops.TensorArray(
        dtypes.float32, handle=handle, flow=flow)
    value = array_ops.placeholder(dtypes.float32)
    ta_grad = ta_grad.write(0, value)
    read_value = ta_grad.read(0)

    # Make sure shape inference worked.
    self.assertIsNone(read_value.shape.ndims)
    # Write with some shape and check read value.
    fed_value = np.random.random([4, 5, 7])
    self.assertAllClose(fed_value,
                        sess.run(read_value, feed_dict={value: fed_value}))
