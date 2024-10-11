# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
# Note: there are additional tests in ragged/ragged_map_fn_op_test.py
with self.cached_session():
    rt = ragged_factory_ops.constant([[1, 2], [3]])
    result = map_fn.map_fn(
        lambda x: x + 1,
        rt,
        fn_output_signature=ragged_tensor.RaggedTensorSpec([None], rt.dtype))
    self.assertAllEqual([[2, 3], [4]], result)
    self.assertEqual([2, None], result.shape.as_list())
