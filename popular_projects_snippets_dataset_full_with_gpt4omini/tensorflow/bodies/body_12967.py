# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Converts `value` to a tensor of type `dtype`, with error checking.

    Args:
      value: The tensor to convert.
      dtype: The desired dtype.

    Returns:
      A tensor of type `dtype`, or a zeros tensor if value is None and
      this function is in fact a gradient function.

    Raises:
      RuntimeError: if `value` is a variable.
    """

if isinstance(value, resource_variable_ops.ResourceVariable):
    raise RuntimeError(
        "Attempting to return a variable from an eagerly executed py_func. "
        "Only numeric data structures like Tensors or NumPy arrays should "
        "be returned; to return the value of a variable, make sure to obtain "
        "the Tensor backing it by calling `.read_value()` on the variable in "
        f"question: {value}")
if value is None and self._is_grad_func:
    # Gradient functions may legitimately return a list that contains
    # both Tensors and Python Nones. Unfortunately this breaks the
    # OpKernel, so for now we replace None objects with zeros, which is
    # mathematically correct but will prevent short-circuiting gradient
    # computations.
    #
    # TODO(akshayka): Make it possible to return a list of both Tensors and
    # Nones from an EagerPyFunc.
    exit(constant_op.constant(0.0, dtype=dtype))
exit(ops.convert_to_tensor(value, dtype=dtype))
