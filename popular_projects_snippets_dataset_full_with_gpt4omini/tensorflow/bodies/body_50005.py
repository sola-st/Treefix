# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Add a new slot variable for `var`.

    A slot variable is an additional variable associated with `var` to train.
    It is allocated and managed by optimizers, e.g. `Adam`.

    Args:
      var: a `Variable` object.
      slot_name: name of the slot variable.
      initializer: initializer of the slot variable
      shape: (Optional) shape of the slot variable. If not set, it will default
      to the shape of `var`.

    Returns:
      A slot variable.
    """
if slot_name not in self._slot_names:
    self._slot_names.append(slot_name)
var_key = _var_key(var)
slot_dict = self._slots.setdefault(var_key, {})
weight = slot_dict.get(slot_name, None)
if weight is None:
    if isinstance(initializer, str) or callable(initializer):
        initializer = initializers.get(initializer)
        if isinstance(
            initializer,
            trackable.CheckpointInitialValueCallable) or (shape is not None):
            slot_shape = shape
        else:
            slot_shape = var.shape
        initial_value = functools.partial(
            initializer, shape=slot_shape, dtype=var.dtype)
    else:
        initial_value = initializer

    with self._distribution_strategy_scope():
        strategy = distribute_ctx.get_strategy()
        if not strategy.extended.variable_created_in_scope(var):
            raise ValueError(
                "Trying to create optimizer slot variable under the scope for "
                "tf.distribute.Strategy ({}), which is different from the scope "
                "used for the original variable ({}). Make sure the slot "
                "variables are created under the same strategy scope. This may "
                "happen if you're restoring from a checkpoint outside the scope"
                .format(strategy, var))

        with strategy.extended.colocate_vars_with(var):
            weight = tf_variables.Variable(
                name="%s/%s" % (var._shared_name, slot_name),  # pylint: disable=protected-access
                dtype=var.dtype,
                trainable=False,
                initial_value=initial_value)
    backend.track_variable(weight)
    slot_dict[slot_name] = weight
    self._restore_slot_variable(
        slot_name=slot_name, variable=var,
        slot_variable=weight)
    self._weights.append(weight)
exit(weight)
