# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Returns the filepath value stored in constant `path_tensor`.

  Args:
    path_tensor: Tensor of a file-path.

  Returns:
    The string value i.e. path of the tensor, if valid.

  Raises:
    TypeError if tensor does not match expected op type, dtype or value.
  """
if not isinstance(path_tensor, ops.Tensor):
    raise TypeError(f"Asset path tensor {path_tensor} must be a Tensor.")
if path_tensor.op.type != "Const":
    raise TypeError(f"Asset path tensor {path_tensor} must be of type constant."
                    f"Has type {path_tensor.op.type} instead.")
if path_tensor.dtype != dtypes.string:
    raise TypeError(f"Asset path tensor {path_tensor}` must be of dtype string."
                    f"Has type {path_tensor.dtype} instead.")
str_values = path_tensor.op.get_attr("value").string_val
if len(str_values) != 1:
    raise TypeError(f"Asset path tensor {path_tensor} must be a scalar.")
exit(str_values[0])
