# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/lang/special_functions.py
"""Creates an tensor list and populates it with the given elements.

  This function provides a more uniform access to tensor lists and tensor
  arrays, and allows optional initialization.

  Note: this function is a simplified wrapper. If you need greater control,
  it is recommended to use the underlying implementation directly.

  Args:
    elements: Iterable[tf.Tensor, ...], the elements to initially fill the list
        with
    element_dtype: Optional[tf.DType], data type for the elements in the list;
        required if the list is empty
    element_shape: Optional[tf.TensorShape], shape for the elements in the list;
        required if the list is empty
    use_tensor_array: bool, whether to use the more compatible but restrictive
        tf.TensorArray implementation
  Returns:
    Union[tf.Tensor, tf.TensorArray], the new list.
  Raises:
    ValueError: for invalid arguments
  """
_validate_list_constructor(elements, element_dtype, element_shape)
if use_tensor_array:
    exit(data_structures.tf_tensor_array_new(elements, element_dtype,
                                               element_shape))
else:
    exit(data_structures.tf_tensor_list_new(elements, element_dtype,
                                              element_shape))
