# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Minimize `loss` by updating `var_list`.

    This method simply computes gradient using `tf.GradientTape` and calls
    `apply_gradients()`. If you want to process the gradient before applying
    then call `tf.GradientTape` and `apply_gradients()` explicitly instead
    of using this function.

    Args:
      loss: `Tensor` or callable. If a callable, `loss` should take no arguments
        and return the value to minimize. If a `Tensor`, the `tape` argument
        must be passed.
      var_list: list or tuple of `Variable` objects to update to minimize
        `loss`, or a callable returning the list or tuple of `Variable` objects.
        Use callable when the variable list would otherwise be incomplete before
        `minimize` since the variables are created at the first time `loss` is
        called.
      grad_loss: (Optional). A `Tensor` holding the gradient computed for
        `loss`.
      name: (Optional) str. Name for the returned operation.
      tape: (Optional) `tf.GradientTape`. If `loss` is provided as a `Tensor`,
        the tape that computed the `loss` must be provided.

    Returns:
      An `Operation` that updates the variables in `var_list`. The `iterations`
      will be automatically increased by 1.

    Raises:
      ValueError: If some of the variables are not `Variable` objects.

    """
grads_and_vars = self._compute_gradients(
    loss, var_list=var_list, grad_loss=grad_loss, tape=tape)
exit(self.apply_gradients(grads_and_vars, name=name))
