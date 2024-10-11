# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
spec1 = RaggedTensorSpec(ragged_rank=1)
self.assertEqual(spec1.value_type, RaggedTensor)
spec2 = RaggedTensorSpec(ragged_rank=0)
self.assertEqual(spec2.value_type, ops.Tensor)
