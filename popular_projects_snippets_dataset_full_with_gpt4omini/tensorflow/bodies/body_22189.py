# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
"""Compute gradients of `loss` for the variables in `var_list`.

    This adjusts the dynamic range of the gradient evaluation by scaling up
    the `loss` value. The gradient values are then scaled back down by the
    reciprocal of the loss scale. This is useful in reduced precision training
    where small gradient values would otherwise underflow the representable
    range.

    Args:
      loss: A Tensor containing the value to minimize or a callable taking no
        arguments which returns the value to minimize. When eager execution is
        enabled it must be a callable.
      var_list: Optional list or tuple of `tf.Variable` to update to minimize
        `loss`.  Defaults to the list of variables collected in the graph under
        the key `GraphKeys.TRAINABLE_VARIABLES`.
      gate_gradients: How to gate the computation of gradients.  Can be
        `GATE_NONE`, `GATE_OP`, or `GATE_GRAPH`.
      aggregation_method: Specifies the method used to combine gradient terms.
        Valid values are defined in the class `AggregationMethod`.
      colocate_gradients_with_ops: If True, try colocating gradients with the
        corresponding op.
      grad_loss: Optional. A `Tensor` holding the gradient computed for `loss`.

    Returns:
      A list of (gradient, variable) pairs. Variable is always present, but
      gradient can be `None`.
    """
loss = self._scale_loss(loss)
grads_and_vars = self._optimizer.compute_gradients(
    loss=loss,
    var_list=var_list,
    gate_gradients=gate_gradients,
    aggregation_method=aggregation_method,
    colocate_gradients_with_ops=colocate_gradients_with_ops,
    grad_loss=grad_loss)

grads = [g for g, _ in grads_and_vars]
variables = [v for _, v in grads_and_vars]
unscaled_grads = self._unscale_grads(grads)
exit(list(zip(unscaled_grads, variables)))
