# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt_spec = RaggedTensorSpec(ragged_rank=2, dtype=dt)
full_type_list = fulltypes_for_flat_tensors(rt_spec)
expect = [
    full_type_pb2.FullTypeDef(
        type_id=full_type_pb2.TFT_RAGGED,
        args=[full_type_pb2.FullTypeDef(type_id=ft)])
]
self.assertEqual(len(rt_spec._flat_tensor_specs), len(full_type_list))
self.assertEqual(expect, full_type_list)
