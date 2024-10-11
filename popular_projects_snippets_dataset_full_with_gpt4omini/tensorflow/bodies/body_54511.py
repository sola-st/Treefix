# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_gradient.py
"""Replaces the gradient components in `value` with `component_grads`.

    Args:
      value: A value with its gradient components compatible with
        `component_grads`.
      component_grads: A nested structure of `Tensor` or `IndexedSlices` or
        `None` (for unconnected gradients).

    Returns:
      A copy of `value`, where the components that should be included in
      gradients have been replaced by `component_grads`; or `None` (if
      `component_grads` includes `None`).
    """
raise NotImplementedError(
    f"{type(self).__name__}.replace_gradient_components()")
