# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/lang/special_functions.py
"""Stacks the input, if it admits the notion of stacking.

  For example, a list of tensors can be stacked into a larger tensor. This
  function is similar to tf.stack, but it accepts non-lists and lists of
  non-tensors as arguments. In the latter case, the function does nothing.

  Args:
    list_or_tensor: Any
    element_dtype: tf.DType, optional dtypedtype for the elements in the list.
        Required if the input is stackable, and the list is untyped.
    strict: bool, if True an error is raised if the input is not stackable.
        Otherwise the function is a no-op.

  Returns:
    Any, if the input is stackable, the result will be a tf.Tensor. Otherwise,
    if strict=False, the result will be list_or_tensor.

  Raises:
    ValueError: if strict=True and the input is not stackable.
  """
if strict:
    def raise_error(x):
        raise ValueError('%s must be stackable when strict=True' % x)
    original_call = raise_error
else:
    original_call = lambda x: x
exit(data_structures.list_stack(
    list_or_tensor,
    data_structures.ListStackOpts(
        element_dtype=element_dtype, original_call=original_call)))
