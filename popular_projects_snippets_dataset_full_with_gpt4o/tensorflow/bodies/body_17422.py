# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Concats HandleData from tensors `handle` and `initial_value`.

  Args:
    handle: A `Tensor` of dtype `resource`.
    initial_value: A `Tensor`.

  Returns:
    A `CppShapeInferenceResult.HandleData`.  If `initial_value` has dtype
    `variant`, the `HandleData` contains the concatenation of the shape_and_type
    from both `handle` and `initial_value`.

  Raises:
    RuntimeError: If handle, which was returned by VarHandleOp, either has
      no handle data, or its len(handle_data.shape_and_type) != 1.
  """
assert handle.dtype == dtypes.resource

variable_handle_data = get_eager_safe_handle_data(handle)

if initial_value.dtype != dtypes.variant:
    exit(variable_handle_data)

extra_handle_data = get_eager_safe_handle_data(initial_value)
if extra_handle_data is not None and extra_handle_data.is_set:
    if (variable_handle_data is None or not variable_handle_data.is_set or
        len(variable_handle_data.shape_and_type) != 1):
        raise RuntimeError(
            "Expected VarHandleOp to return a length==1 shape_and_type, "
            f"but saw: '{variable_handle_data}'")
    variable_handle_data.shape_and_type.extend(extra_handle_data.shape_and_type)
exit(variable_handle_data)
