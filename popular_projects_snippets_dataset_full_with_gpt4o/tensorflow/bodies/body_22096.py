# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
"""Maintains moving averages of variables.

    `var_list` must be a list of `Variable` objects.  This method
    creates shadow variables (holding the moving averages)
    for all elements of `var_list`, and
    updates the moving averages using the current `var_list` values. Shadow
    variables for `Variable` objects are initialized to the variable's initial
    value.

    Shadow variables are created with `trainable=False`. To access them you
    can use the EMA object's `average` method. Note that `EMA` objects are
    not trackable by checkpoints, so if you want to checkpoint or restore the
    moving variables you will need to manually grab the shadow
    variables via `average()` and assign them as `tf.Module` properties or
    directly pass them to your `tf.train.Checkpoint`.

    Note that `apply()` can be called multiple times. When eager execution is
    enabled each call to apply will update the variables once, so this needs to
    be called in a loop.

    In legacy TF 1.x graphs, this method returns an op that updates all
    shadow variables from the current value of their associated variables. In
    TF 1.x graphs without automatically control dependencies this op needs to be
    manually run.

    Args:
      var_list: A list of Variable objects. The variables
        must be of types bfloat16, float16, float32, or float64.
        (In legacy TF 1.x graphs these may be tensors, but this is unsupported
        when eager execution is enabled.)

    Returns:
      An Operation that updates the moving averages.

    Raises:
      TypeError: If the arguments are not an allowed type.
    """
# TODO(touts): op_scope
if var_list is None:
    var_list = variables.trainable_variables()
for v in var_list:
    if (isinstance(v, ops.Tensor)
        and ops.executing_eagerly_outside_functions()):
        raise TypeError(
            "tf.train.ExponentialMovingAverage does not support non-Variable"
            " tensors when eager execution is enabled.")
zero_debias_true = set()  # set of vars to set `zero_debias=True`
for var in var_list:
    if var.dtype.base_dtype not in [
        dtypes.bfloat16, dtypes.float16, dtypes.float32, dtypes.float64
    ]:
        raise TypeError("The variables must be half, float, or double: %s" %
                        var.name)

    if var.ref() not in self._averages:
        # For variables: to lower communication bandwidth across devices we keep
        # the moving averages on the same device as the variables. For other
        # tensors, we rely on the existing device allocation mechanism.
        with ops.init_scope():
            if isinstance(var, variables.Variable):
                with ops.device(var.device):
                    initialized_value = var.initialized_value()
                avg = slot_creator.create_slot(
                    var,
                    initialized_value,
                    self.name,
                    colocate_with_primary=True,
                    copy_xla_sharding=True)
                # NOTE(mrry): We only add `tf.Variable` objects to the
                # `MOVING_AVERAGE_VARIABLES` collection.
                ops.add_to_collection(ops.GraphKeys.MOVING_AVERAGE_VARIABLES, var)
            else:
                avg = slot_creator.create_zeros_slot(
                    var,
                    self.name,
                    colocate_with_primary=(var.op.type in [
                        "Variable", "VariableV2", "VarHandleOp"
                    ]),
                    copy_xla_sharding=True)
                if self._zero_debias:
                    zero_debias_true.add(avg.ref())
        self._averages[var.ref()] = avg

with ops.name_scope(self.name) as scope:
    decay = ops.convert_to_tensor(
        self._decay, dtype=dtypes.float32, name="decay")
    if self._num_updates is not None:
        num_updates = math_ops.cast(
            self._num_updates, dtypes.float32, name="num_updates")
        decay = math_ops.minimum(decay,
                                 (1.0 + num_updates) / (10.0 + num_updates))
    updates = []
    for var in var_list:
        avg = self._averages[var.ref()]
        zero_debias = avg.ref() in zero_debias_true
        updates.append(assign_moving_average(avg, var, decay, zero_debias))
    exit(control_flow_ops.group(*updates, name=scope))
