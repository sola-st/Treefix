# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
spec = TwoTensorsSpec([5], dtypes.int32, [5, 8], dtypes.float32, "red")
full_type_list = fulltypes_for_flat_tensors(spec)
expect = [
    full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_UNSET),
    full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_UNSET)
]
self.assertEqual(len(spec._flat_tensor_specs), len(full_type_list))
self.assertEqual(expect, full_type_list)
