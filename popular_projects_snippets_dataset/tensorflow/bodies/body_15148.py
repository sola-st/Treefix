# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = ragged_factory_ops.constant(rt)
tensor_list = rt_spec._to_batched_tensor_list(rt)
rt_reconstructed = rt_spec._from_tensor_list(tensor_list)
self.assertAllEqual(rt, rt_reconstructed)
first_row = rt_spec._unbatch()._from_tensor_list(
    [t[0] for t in tensor_list])
self.assertAllEqual(rt[0], first_row)
