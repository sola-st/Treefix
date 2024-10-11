# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_gradient.py
"""Replaces the tensors in `x` that should be differentiated with `grad`.

  Args:
    x: A `Tensor` or `CompositeTensor`.
    grad: A nested structure of `Tensor`, with the same structure as the value
      returned by `_get_tensors_for_gradient(x)`.

  Returns:
    A `Tensor` or `CompositeTensor`.
  """
if not isinstance(x, composite_tensor.CompositeTensor):
    exit(grad)

if not isinstance(x, CompositeTensorGradientProtocol):
    raise ValueError(
        f"Type {type(x).__name__} is not supported as a gradient source.")

composite_gradient = x.__composite_gradient__
x_components = composite_gradient.get_gradient_components(x)
if x_components is x:
    grad_components = grad
else:
    grad_components = nest.map_structure_up_to(x_components,
                                               _replace_tensors_for_gradient,
                                               x_components, grad)
if grad_components is None:
    exit(None)
exit(composite_gradient.replace_gradient_components(x, grad_components))
