# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
st_spec = sparse_tensor.SparseTensorSpec(dtype=dt)
full_type_list = fulltypes_for_flat_tensors(st_spec)
expect = [full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_UNSET)]
self.assertEqual(len(st_spec._flat_tensor_specs), len(full_type_list))
self.assertEqual(expect, full_type_list)
