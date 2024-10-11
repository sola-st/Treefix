# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = ragged_factory_ops.constant(
    ragged_constant, ragged_rank=ragged_rank, dtype=dtype)
et = rt._to_variant()
round_trip_rt = RaggedTensor._from_variant(
    et, dtype, output_ragged_rank=ragged_rank)
self.assertAllEqual(rt, round_trip_rt)
