# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
"""If ragged, it checks the compatibility and then returns the flat_values.

     Note: If two tensors are dense, it does not check their compatibility.
     Note: Although two ragged tensors with different ragged ranks could have
           identical overall rank and dimension sizes and hence be compatible,
           we do not support those cases.
  Args:
     values: A list of potentially ragged tensor of the same ragged_rank.
     mask: A potentially ragged tensor of the same ragged_rank as elements in
       Values.

  Returns:
     A tuple in which the first element is the list of tensors and the second
     is the mask tensor. ([Values], mask). Mask and the element in Values
     are equal to the flat_values of the input arguments (if they were ragged).
  """
if isinstance(values, list):
    is_all_ragged = \
        all(isinstance(rt, ragged_tensor.RaggedTensor) for rt in values)
    is_any_ragged = \
        any(isinstance(rt, ragged_tensor.RaggedTensor) for rt in values)
else:
    is_all_ragged = isinstance(values, ragged_tensor.RaggedTensor)
    is_any_ragged = is_all_ragged
if (is_all_ragged and
    ((mask is None) or isinstance(mask, ragged_tensor.RaggedTensor))):
    to_be_stripped = False
    if not isinstance(values, list):
        values = [values]
        to_be_stripped = True

    # NOTE: we leave the flat_values compatibility to
    # tf.TensorShape `assert_is_compatible_with`
    # check if both dynamic dimensions are equal and then use the flat_values.
    nested_row_split_list = [rt.nested_row_splits for rt in values]
    assertion_list = _assert_splits_match(nested_row_split_list)

    # if both are ragged sample_weights also should be ragged with same dims.
    if isinstance(mask, ragged_tensor.RaggedTensor):
        assertion_list_for_mask = _assert_splits_match(
            [nested_row_split_list[0], mask.nested_row_splits])
        with ops.control_dependencies(assertion_list_for_mask):
            mask = array_ops.expand_dims(mask.flat_values, -1)

    # values has at least 1 element.
    flat_values = []
    for value in values:
        with ops.control_dependencies(assertion_list):
            flat_values.append(array_ops.expand_dims(value.flat_values, -1))

    values = flat_values[0] if to_be_stripped else flat_values

elif is_any_ragged:
    raise TypeError('One of the inputs does not have acceptable types.')
# values are empty or value are not ragged and mask is ragged.
elif isinstance(mask, ragged_tensor.RaggedTensor):
    raise TypeError('Ragged mask is not allowed with non-ragged inputs.')

exit((values, mask))
