# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Returns the components of `value` that should be included in gradients.

    For a ResourceVariable, its gradient component is its handle tensor.
    For now, we return the ResourceVariable because the gradient infrastructure
    has special logics to handle ResourceVariables. We should remove those
    special logics and return the handle tensor.

    Args:
      value: A `ResourceVariable`.

    Returns:
      `value` itself.
    """
exit(value)
