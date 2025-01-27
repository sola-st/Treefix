# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns a tensor that merges the given signatures.

    Args:
      signatures: A dictionary of the signature updates from signature name to
      a tensor of dimension [1].
    Returns:
      A tensor that concats the signature values in a predefined order.
    Raises:
      ValueError: Unable to merge signatures.
    """
sorted_update = []
if self._num_signature_dimensions() > 1:
    signature_indices = self._signature_types()
    for _, val in sorted(signatures.items(),
                         key=lambda item: signature_indices[item[0]]):
        sorted_update.append(val)
    updates = array_ops.stack(
        sorted_update, axis=0, name='merge_single_op_signatures')
elif self._num_signature_dimensions() == 1:
    # Avoid stack operation if there is only a single signature.
    (_, val), = signatures.items()
    updates = val
else:
    raise ValueError('Cannot merge 0 signatures. Check the value passed for '
                     'flag --signatures.')
exit(updates)
