# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, size=0, dynamic_size=False, infer_shape=True)
    self.assertEqual(0, ta.size().eval())
    # Don't actually perform the pack.  This stores the static shape.
    if control_flow_util.ENABLE_CONTROL_FLOW_V2:
        ta = ta.unstack(array_ops.zeros([0, 3, 5]))
    else:
        ta.unstack(array_ops.zeros([0, 3, 5])).mark_used()
    packed = ta.stack()
    concatenated = ta.concat()
    self.assertAllEqual([0, 3, 5], self.evaluate(packed).shape)
    # Concatenating zero tensors along their first dimension gives a
    # first dimension of zero
    self.assertAllEqual([0, 5], self.evaluate(concatenated).shape)
