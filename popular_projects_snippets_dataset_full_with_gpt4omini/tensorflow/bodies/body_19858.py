# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Merges the given caches on tpu.

    Args:
      global_tt_summary_cache: The global tensor tracer summary cache tensor
        with shape (num_cores, num_traced_tensors, num_traced_signatures). First
        dimension corresponds to core_id, where global_tpu_cache_tensor[i]
        correspond to the local cache from core-i.
    Returns:
      An aggregated tf.Tensor.
    Raises:
      RuntimeError: if there is no aggregate function defined for a signature.
    """

# Merge only statistics tensor, if it is any other tensor we simply,
# concatenate them.
agg_fn_map = self._parameters.get_signature_to_agg_fn_map()
signature_idx_map = self._signature_types()
aggregation_result = []
for signature, idx in sorted(signature_idx_map.items(),
                             key=operator.itemgetter(1)):
    if signature not in agg_fn_map:
        raise RuntimeError('No aggregation function is defined for '
                           'signature %s.' % signature)
    # The dimensions of the statistics tensor is
    # num_cores x num_traced_tensors x num_signatures
    # value[:,:,idx] will return the portion of the tensor related
    # to signature.
    signature_tensor = global_tt_summary_cache[:, :, idx]
    # Merge it along the first (core) axis.
    agg_fn = agg_fn_map[signature]
    agg_tensor = agg_fn(signature_tensor, axis=0)
    aggregation_result.append(agg_tensor)
# Merge results corresponding to different signatures

merged_signatures = array_ops.stack(aggregation_result)
# merged_signatures has dimensions
# num_signatures x num_traced_tensors, transpose it so that it
# will match with the original structure
# num_traced_tensors x num_signatures.
transposed_signatures = array_ops.transpose(merged_signatures)
# Expand 1 more dimension so that it will match with the expected
# structure num_cores x num_traced_tensors x num_signatures.
exit(array_ops.expand_dims(transposed_signatures, axis=0))
