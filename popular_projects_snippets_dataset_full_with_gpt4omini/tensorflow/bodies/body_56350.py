# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec = tensor_spec.TensorSpec([1], np.float32)
full_type_list = fulltypes_for_flat_tensors(spec)
expect = [full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_UNSET)]
self.assertEqual(len(spec._flat_tensor_specs), len(full_type_list))
self.assertEqual(expect, full_type_list)
