# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Compute gradients of `loss` for the variables in `var_list`.

    This is the first part of `minimize()`.  It returns a list
    of (gradient, variable) pairs where "gradient" is the gradient
    for "variable".  Note that "gradient" can be a `Tensor`, an
    `IndexedSlices`, or `None` if there is no gradient for the
    given variable.

    Args:
      loss: `Tensor` or callable. If a callable, `loss` should take no
        arguments and return the value to minimize. If a `Tensor`, the `tape`
        argument must be passed.
      var_list: list or tuple of `Variable` objects to update to minimize
        `loss`, or a callable returning the list or tuple of `Variable` objects.
        Use callable when the variable list would otherwise be incomplete before
        `minimize` and the variables are created at the first time when `loss`
        is called.
      grad_loss: Optional. A `Tensor` holding the gradient computed for `loss`.
      tape: (Optional) `tf.GradientTape`. If `loss` is provided as a `Tensor`,
        the tape that computed the `loss` must be provided.

    Returns:
      A list of (gradient, variable) pairs. Variable is always present, but
      gradient can be `None`.

    Raises:
      TypeError: If `var_list` contains anything else than `Variable` objects.
      ValueError: If some arguments are invalid, or var_list is None.
    """
# TODO(josh11b): Test that we handle weight decay in a reasonable way.
if not callable(loss) and tape is None:
    raise ValueError("`tape` is required when a `Tensor` loss is passed.")
tape = tape if tape is not None else backprop.GradientTape()

if callable(loss):
    with tape:
        if not callable(var_list):
            tape.watch(var_list)
        loss = loss()
        if callable(var_list):
            var_list = var_list()

with tape:
    loss = self._transform_loss(loss)

var_list = nest.flatten(var_list)
with ops.name_scope_v2(self._name + "/gradients"):
    grads_and_vars = self._get_gradients(tape, loss, var_list, grad_loss)

self._assert_valid_dtypes([
    v for g, v in grads_and_vars
    if g is not None and v.dtype != dtypes.resource
])

exit(grads_and_vars)
