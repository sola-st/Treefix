# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
x = MaskedTensorV2([4, 5], [True, False])
spec = type_spec.type_spec_from_value(x)
full_type_list = fulltypes_for_flat_tensors(spec)
expect = [
    full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_UNSET),
    full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_UNSET)
]
self.assertEqual(len(spec._flat_tensor_specs), len(full_type_list))
self.assertEqual(expect, full_type_list)
