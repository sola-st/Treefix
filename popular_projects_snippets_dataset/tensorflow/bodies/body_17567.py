# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_impl.py
"""Multiply the Hessian of `ys` wrt `xs` by `v`.

  This is an efficient construction that uses a backprop-like approach
  to compute the product between the Hessian and another vector. The
  Hessian is usually too large to be explicitly computed or even
  represented, but this method allows us to at least multiply by it
  for the same big-O cost as backprop.

  Implicit Hessian-vector products are the main practical, scalable way
  of using second derivatives with neural networks. They allow us to
  do things like construct Krylov subspaces and approximate conjugate
  gradient descent.

  Example: if `y` = 1/2 `x`^T A `x`, then `hessian_vector_product(y,
  x, v)` will return an expression that evaluates to the same values
  as (A + A.T) `v`.

  Args:
    ys: A scalar value, or a tensor or list of tensors to be summed to
        yield a scalar.
    xs: A list of tensors that we should construct the Hessian over.
    v: A list of tensors, with the same shapes as xs, that we want to
       multiply by the Hessian.

  Returns:
    A list of tensors (or if the list would be length 1, a single tensor)
    containing the product between the Hessian and `v`.

  Raises:
    ValueError: `xs` and `v` have different length.

  """

# Validate the input
length = len(xs)
if len(v) != length:
    raise ValueError("xs and v must have the same length.")

# First backprop
grads = gradients(ys, xs)

assert len(grads) == length
elemwise_products = [
    math_ops.multiply(grad_elem, array_ops.stop_gradient(v_elem))
    for grad_elem, v_elem in zip(grads, v)
    if grad_elem is not None
]

# Second backprop
exit(gradients(elemwise_products, xs))
