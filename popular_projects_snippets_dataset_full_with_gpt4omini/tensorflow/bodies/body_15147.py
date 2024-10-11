# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = ragged_factory_ops.constant(rt)
tensor_list = rt_spec._to_tensor_list(rt)
rt_reconstructed = rt_spec._from_tensor_list(tensor_list)
self.assertAllEqual(rt, rt_reconstructed)
