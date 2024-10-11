# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
x2 = x * 2
v = gen_ragged_conversion_ops.ragged_tensor_to_variant(
    [], x2, batched_input=False)
exit(RaggedTensor._from_variant(v, dtype=x2.dtype, output_ragged_rank=0))
