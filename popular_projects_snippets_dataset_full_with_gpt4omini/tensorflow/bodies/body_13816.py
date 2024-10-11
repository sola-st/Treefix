# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Subclass implementation of `inverse_log_det_jacobian` public function.

    In particular, this method differs from the public function, in that it
    does not take `event_ndims`. Thus, this implements the minimal Jacobian
    determinant calculation (i.e. over `inverse_min_event_ndims`).

    Args:
      y: `Tensor`. The input to the "inverse_log_det_jacobian" evaluation.
    Returns:
      inverse_log_det_jacobian: `Tensor`, if this bijector is injective.
        If not injective, returns the k-tuple containing jacobians for the
        unique `k` points `(x1, ..., xk)` such that `g(xi) = y`.
    """
raise NotImplementedError("inverse_log_det_jacobian not implemented.")
