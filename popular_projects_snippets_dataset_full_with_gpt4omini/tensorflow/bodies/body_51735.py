# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
x = ragged_factory_ops.constant([[1, 2], [3]])
x_tensor_info = utils.build_tensor_info(x)
# Check components
self.assertEqual(x.values.name,
                 x_tensor_info.composite_tensor.components[0].name)
self.assertEqual(types_pb2.DT_INT32,
                 x_tensor_info.composite_tensor.components[0].dtype)
self.assertEqual(x.row_splits.name,
                 x_tensor_info.composite_tensor.components[1].name)
self.assertEqual(types_pb2.DT_INT64,
                 x_tensor_info.composite_tensor.components[1].dtype)
# Check type_spec.
spec_proto = struct_pb2.StructuredValue(
    type_spec_value=x_tensor_info.composite_tensor.type_spec)
spec = nested_structure_coder.decode_proto(spec_proto)
self.assertEqual(spec, x._type_spec)
