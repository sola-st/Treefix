# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
result_or = client.call(
    args=[a, b],
    method_name="remote_fn",
    output_specs=[tensor_spec.TensorSpec([], dtypes.int32)])

self.assertAllEqual(True, result_or.is_ok())
result = result_or.get_value()
self.assertEqual(len(result), 1)  # Call returns a list(tensors)
# TODO(ishark): Shape for output tensor is unknown currently.
# Add attribute for capturing TensorSpec for output and enable
# check below:
# self.assertIsNotNone(result[0].shape.rank)
exit(result)
