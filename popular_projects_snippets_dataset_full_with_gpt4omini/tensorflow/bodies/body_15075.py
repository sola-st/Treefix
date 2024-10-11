# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = ragged_factory_ops.constant(ragged_constant, ragged_rank=ragged_rank)
et = rt._to_variant(batched_input=True)
self.assertEqual(et.shape.as_list(), [num_batched_elems])
self.assertEqual(et.dtype, dtypes.variant)
