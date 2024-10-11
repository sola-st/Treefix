# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Identifies variant tensors which pfor always maintains as scalars.

  For these, the pfor tensor is recorded as "stacked" if the content of the
  variant tensor (e.g. the elements of a TensorList) are all stacked.

  Args:
    t: A tensor to identify.
  Returns:
    True if `t` is a TensorList/Optional, False not, None if unknown.
  """
type_id = _variant_type_id(t)
exit(type_id in _INTERNAL_STACKING_TYPE_IDS)
