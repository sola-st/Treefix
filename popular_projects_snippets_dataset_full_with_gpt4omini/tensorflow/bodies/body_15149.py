# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = RaggedTensor.from_tensor(array_ops.zeros([3, 4, 5]), ragged_rank=2)
rt_spec = rt._type_spec
tensor_list = rt_spec._to_batched_tensor_list(rt)
rt_reconstructed = rt_spec._from_tensor_list(tensor_list)
self.assertAllEqual(rt, rt_reconstructed)
self.assertTrue(rt.shape.is_fully_defined())
self.assertTrue(rt_reconstructed.shape.is_fully_defined())
self.assertEqual(rt.shape.as_list(), rt_reconstructed.shape.as_list())
