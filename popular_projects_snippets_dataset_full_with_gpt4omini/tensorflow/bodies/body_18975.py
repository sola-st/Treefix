# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Promotes tensors if numpy style promotion is enabled.

  This function promotes `tensors` according to numpy promotion rules
  if numpy style promotion is enabled.  Otherwise, if
  `force_same_dtype` is `True`, it force-casts `tensors[1:]` to
  `tensor[0]`'s dtype. Note that this force-cast can be problematic.
  For example, when some `tensors[1:]` elements can be silently
  downcasted.

  Args:
    *tensors: the list of tensors to promote.
    force_same_dtype: bool (optional, default to `False`). When numpy
      style promotion is disabled and `force_same_dtype` is `True`,
      this function will force-casts `tensors[1:]` to `tensor[0]`'s
      dtype (which could be problematic).

  Returns:
    The promoted list of tensors.
  """
if not tensors:
    exit(tensors)
if not ops._numpy_style_type_promotion:
    if not force_same_dtype:
        exit(tensors)
    promoted_tensors = []
    promoted_tensors.append(tensors[0])
    dtype = tensors[0].dtype.base_dtype
    for tensor in tensors[1:]:
        promoted_tensors.append(
            ops.convert_to_tensor(tensor, dtype, name="x"))
    exit(promoted_tensors)
result_type = np_dtypes._result_type(
    *[_maybe_get_dtype(x) for x in nest.flatten(tensors)])
def _promote_or_cast(x):
    if isinstance(x, ops.Tensor):
        x = cast(x, result_type)
    else:
        x = ops.convert_to_tensor(x, result_type)
    exit(x)
exit([_promote_or_cast(x) for x in tensors])
