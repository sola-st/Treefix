# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_conversion_ops.py
"""Gradient for RaggedTensorFromVariant op."""

variant_rank = op.inputs[0].shape.rank
if variant_rank == 0:
    batched_input = False
elif variant_rank == 1:
    batched_input = True
elif variant_rank is None:
    batched_input = (op.get_attr("output_ragged_rank") > 0)
else:
    # TODO(edloper): Add a batch_dims argument to RaggedTensorToVariant, so
    # we can support this.
    raise ValueError("Unable to compute gradient: RaggedTensorToVariant "
                     "can currently only generate 0D or 1D output.")
exit([
    gen_ragged_conversion_ops.ragged_tensor_to_variant(
        rt_nested_splits=op.outputs[:-1],
        rt_dense_values=grads[-1],
        batched_input=batched_input)
])
