# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_gradient.py
"""Returns the components of `value` that should be included in gradients.

    This method may not call TensorFlow ops, since any new ops added to the
    graph would not be propertly tracked by the gradient mechanisms.

    Args:
      value: A `CompositeTensor` value.

    Returns:
      A nested structure of `Tensor` or `IndexedSlices`.
    """
raise NotImplementedError(
    f"{type(self).__name__}.get_gradient_components()")
