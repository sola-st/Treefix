# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
a = TwoComposites(
    ragged_factory_ops.constant([[1, 2], [3]]),
    ragged_factory_ops.constant([[5], [6, 7, 8]]))
a_spec = type_spec.type_spec_from_value(a)
full_type_list = fulltypes_for_flat_tensors(a_spec)
expect = [
    full_type_pb2.FullTypeDef(
        type_id=full_type_pb2.TFT_RAGGED,
        args=[full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_INT32)]),
    full_type_pb2.FullTypeDef(
        type_id=full_type_pb2.TFT_RAGGED,
        args=[full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_INT32)]),
]
self.assertEqual(len(a_spec._flat_tensor_specs), len(full_type_list))
self.assertEqual(expect, full_type_list)
