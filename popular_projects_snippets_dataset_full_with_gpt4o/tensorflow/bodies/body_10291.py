# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
"""Computes the gradient error for float16 inputs and/or outputs.

    This returns the same value as gradient_checker.compute_gradient_error. The
    difference is that gradient_checker.compute_gradient_error does not
    numerically compute the gradients in a numerically stable way for float16
    tensors. To fix this, this function requires float32 versions of x and y to
    numerically compute the gradients, to compare with the float16 symbolically
    computed gradients.

    Args:
      x: The input tensor.
      x32: A float32 version of x.
      x_shape: The shape of x.
      y: The output tensor.
      y32: A float32 version of y. Must be calculated based on x32, not x.
      y_shape: The shape of y.
      x_dtype: The type of x, float16 or bfloat16.

    Returns:
      The maximum error in between the two Jacobians, as in
      gradient_checker.compute_gradient_error.
    """
x_init_val = np.random.random_sample(x_shape).astype(x_dtype)
x32_init_val = x_init_val.astype(np.float32)

# TODO(reedwm): Do not perform the unnecessary computations in
# compute_gradient, since they double the computation time of this function.
theoretical_grad, _ = gradient_checker.compute_gradient(
    x, x_shape, y, y_shape, delta=1e-3, x_init_value=x_init_val)
_, numerical_grad = gradient_checker.compute_gradient(
    x32, x_shape, y32, y_shape, delta=1e-3, x_init_value=x32_init_val)

# If grad is empty, no error.
if theoretical_grad.size == 0 and numerical_grad.size == 0:
    exit(0)
exit(np.fabs(theoretical_grad - numerical_grad).max())
