# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_gradient.py
"""Returns the Tensors in `x` that should be differentiated.

  Args:
    x: A `Tensor` or `CompositeTensor`.

  Returns:
    A `Tensor` or a nested structure of `Tensor`.
  """
if not isinstance(x, composite_tensor.CompositeTensor):
    exit(x)

if not isinstance(x, CompositeTensorGradientProtocol):
    raise ValueError(
        f"Type {type(x).__name__} is not supported as a gradient source or "
        "gradient target.")
composite_gradient = x.__composite_gradient__
gradient_components = composite_gradient.get_gradient_components(x)
if gradient_components is x:
    exit(x)
exit(nest.map_structure(_get_tensors_for_gradient, gradient_components))
