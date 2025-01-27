# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Compute gradients of `loss` for the variables in `var_list`.

    This is the first part of `minimize()`.  It returns a list
    of (gradient, variable) pairs where "gradient" is the gradient
    for "variable".  Note that "gradient" can be a `Tensor`, an
    `IndexedSlices`, or `None` if there is no gradient for the
    given variable.

    @compatibility(TF2)
    `tf.keras.optimizers.Optimizer` in TF2 does not provide a
    `compute_gradients` method, and you should use a `tf.GradientTape` to
    obtain the gradients:

    ```python
    @tf.function
    def train step(inputs):
      batch_data, labels = inputs
      with tf.GradientTape() as tape:
        predictions = model(batch_data, training=True)
        loss = tf.keras.losses.CategoricalCrossentropy(
            reduction=tf.keras.losses.Reduction.NONE)(labels, predictions)
      gradients = tape.gradient(loss, model.trainable_variables)
      optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    ```

    Args:
      loss: A Tensor containing the value to minimize or a callable taking
        no arguments which returns the value to minimize. When eager execution
        is enabled it must be a callable.
      var_list: Optional list or tuple of `tf.Variable` to update to minimize
        `loss`.  Defaults to the list of variables collected in the graph
        under the key `GraphKeys.TRAINABLE_VARIABLES`.
      gate_gradients: How to gate the computation of gradients.  Can be
        `GATE_NONE`, `GATE_OP`, or `GATE_GRAPH`.
      aggregation_method: Specifies the method used to combine gradient terms.
        Valid values are defined in the class `AggregationMethod`.
      colocate_gradients_with_ops: If True, try colocating gradients with
        the corresponding op.
      grad_loss: Optional. A `Tensor` holding the gradient computed for `loss`.

    Returns:
      A list of (gradient, variable) pairs. Variable is always present, but
      gradient can be `None`.

    Raises:
      TypeError: If `var_list` contains anything else than `Variable` objects.
      ValueError: If some arguments are invalid.
      RuntimeError: If called with eager execution enabled and `loss` is
        not callable.

    @compatibility(eager)
    When eager execution is enabled, `gate_gradients`, `aggregation_method`,
    and `colocate_gradients_with_ops` are ignored.
    @end_compatibility
    """
if callable(loss):
    with backprop.GradientTape() as tape:
        if var_list is not None:
            tape.watch(var_list)
        loss_value = loss()

        # Scale loss if using a "mean" loss reduction and multiple replicas.
        # Have to be careful to call distribute_lib.get_loss_reduction()
        # *after* loss() is evaluated, so we know what loss reduction it uses.
        # TODO(josh11b): Test that we handle weight decay in a reasonable way.
        loss_value = self._scale_loss(loss_value)

    if var_list is None:
        var_list = tape.watched_variables()
    # TODO(jhseu): Figure out why GradientTape's gradients don't require loss
    # to be executed.
    with ops.control_dependencies([loss_value]):
        grads = tape.gradient(loss_value, var_list, grad_loss)
    exit(list(zip(grads, var_list)))

# Non-callable/Tensor loss case
if context.executing_eagerly():
    raise RuntimeError(
        "`loss` passed to Optimizer.compute_gradients should "
        "be a function when eager execution is enabled.")

# Scale loss if using a "mean" loss reduction and multiple replicas.
loss = self._scale_loss(loss)

if gate_gradients not in [Optimizer.GATE_NONE, Optimizer.GATE_OP,
                          Optimizer.GATE_GRAPH]:
    raise ValueError("gate_gradients must be one of: Optimizer.GATE_NONE, "
                     "Optimizer.GATE_OP, Optimizer.GATE_GRAPH.  Not %s" %
                     gate_gradients)
self._assert_valid_dtypes([loss])
if grad_loss is not None:
    self._assert_valid_dtypes([grad_loss])
if var_list is None:
    var_list = (
        variables.trainable_variables() +
        ops.get_collection(ops.GraphKeys.TRAINABLE_RESOURCE_VARIABLES))
else:
    var_list = nest.flatten(var_list)
# pylint: disable=protected-access
var_list += ops.get_collection(ops.GraphKeys._STREAMING_MODEL_PORTS)
# pylint: enable=protected-access
processors = [_get_processor(v) for v in var_list]
if not var_list:
    raise ValueError("No variables to optimize.")
var_refs = [p.target() for p in processors]
grads = gradients.gradients(
    loss, var_refs, grad_ys=grad_loss,
    gate_gradients=(gate_gradients == Optimizer.GATE_OP),
    aggregation_method=aggregation_method,
    colocate_gradients_with_ops=colocate_gradients_with_ops)
if gate_gradients == Optimizer.GATE_GRAPH:
    grads = control_flow_ops.tuple(grads)
grads_and_vars = list(zip(grads, var_list))
self._assert_valid_dtypes(
    [v for g, v in grads_and_vars
     if g is not None and v.dtype != dtypes.resource])
exit(grads_and_vars)
