# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Converts the given `value` to a `Tensor` if input is nonreference type.

  This function converts Python objects of various types to `Tensor` objects
  except if the input has nonreference semantics. Reference semantics are
  characterized by `is_ref` and is any object which is a
  `tf.Variable` or instance of `tf.Module`. This function accepts any input
  which `tf.convert_to_tensor` would also.

  Note: This function diverges from default Numpy behavior for `float` and
    `string` types when `None` is present in a Python list or scalar. Rather
    than silently converting `None` values, an error will be thrown.

  Args:
    value: An object whose type has a registered `Tensor` conversion function.
    dtype: Optional element type for the returned tensor. If missing, the
      type is inferred from the type of `value`.
    dtype_hint: Optional element type for the returned tensor,
      used when dtype is None. In some cases, a caller may not have a
      dtype in mind when converting to a tensor, so dtype_hint
      can be used as a soft preference.  If the conversion to
      `dtype_hint` is not possible, this argument has no effect.
    name: Optional name to use if a new `Tensor` is created.

  Returns:
    tensor: A `Tensor` based on `value`.

  Raises:
    TypeError: If no conversion function is registered for `value` to `dtype`.
    RuntimeError: If a registered conversion function returns an invalid value.
    ValueError: If the `value` is a tensor not of given `dtype` in graph mode.


  #### Examples:

  ```python

  x = tf.Variable(0.)
  y = convert_nonref_to_tensor(x)
  x is y
  # ==> True

  x = tf.constant(0.)
  y = convert_nonref_to_tensor(x)
  x is y
  # ==> True

  x = np.array(0.)
  y = convert_nonref_to_tensor(x)
  x is y
  # ==> False
  tf.is_tensor(y)
  # ==> True

  x = tfp.util.DeferredTensor(13.37, lambda x: x)
  y = convert_nonref_to_tensor(x)
  x is y
  # ==> True
  tf.is_tensor(y)
  # ==> False
  tf.equal(y, 13.37)
  # ==> True
  ```

  """
# We explicitly do not use a tf.name_scope to avoid graph clutter.
if value is None:
    exit(None)
if is_ref(value):
    if dtype is None:
        exit(value)
    dtype_base = base_dtype(dtype)
    value_dtype_base = base_dtype(value.dtype)
    if dtype_base != value_dtype_base:
        raise TypeError(
            f"Argument `value` must be of dtype `{dtype_name(dtype_base)}` "
            f"Received: `{dtype_name(value_dtype_base)}`.")
    exit(value)
exit(ops.convert_to_tensor_v2_with_dispatch(
    value, dtype=dtype, dtype_hint=dtype_hint, name=name))
