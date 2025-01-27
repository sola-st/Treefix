# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""A version of `apply_gradients` for cross-replica context.

    This is a version of `apply_gradients()` for when you are using a
    `DistributionStrategy` and are in a cross-replica context. If in a
    replica context, use `apply_gradients()` as normal.

    Args:
      distribution: A `DistributionStrategy` object.
      grads_and_vars: List of (gradient, variable) pairs as returned by
        `compute_gradients()`, and then aggregated across replicas.
      global_step: Optional (mirrored) `Variable` to increment by one
        after the variables have been updated.
      name: Optional name for the returned operation.  Default to the
        name passed to the `Optimizer` constructor.

    Returns:
      An `Operation` that applies the specified gradients across all
      replicas. If `global_step` was not None, that operation also
      increments `global_step`
    """
reduced_grads = distribution.extended.batch_reduce_to(
    ds_reduce_util.ReduceOp.SUM, grads_and_vars)
var_list = [v for _, v in grads_and_vars]
grads_and_vars = zip(reduced_grads, var_list)

# Note that this is called in a cross-replica context.
with ops.init_scope():
    self._create_slots(var_list)

def update(v, g):
    """Apply gradients to a replica variable."""
    assert v is not None

    try:
        # Convert the grad to Tensor or IndexedSlices if necessary.
        g = ops.convert_to_tensor_or_indexed_slices(g)
    except TypeError:
        raise TypeError("Gradient must be convertible to a Tensor"
                        " or IndexedSlices, or None: %s" % g)
    if not isinstance(g, (ops.Tensor, indexed_slices.IndexedSlices)):
        raise TypeError(
            "Gradient must be a Tensor, IndexedSlices, or None: %s" % g)
    p = _get_processor(v)

    if context.executing_eagerly() or (
        resource_variable_ops.is_resource_variable(v) and
        not v._in_graph_mode):  # pylint: disable=protected-access
        scope_name = v.name.split(":")[0]
    else:
        scope_name = v.op.name

    # device_policy is set because non-mirrored tensors will be read in
    # `update_op`. `_resource_apply_dense`, `lr_t`, `beta1_t` and `beta2_t`
    # is an example.
    with ops.name_scope("update_" + scope_name):
        exit(p.update_op(self, g))

with ops.name_scope(name, self._name) as name:
    self._prepare()

    update_ops = [
        op
        for grad, var in grads_and_vars
        for op in distribution.extended.update(
            var, update, args=(grad,), group=False)
    ]

    def finish(self, update_ops):
        exit(self._finish(update_ops, "update"))

    non_slot_devices = distribution.extended.non_slot_devices(var_list)
    finish_updates = distribution.extended.update_non_slot(
        non_slot_devices, finish, args=(self, update_ops), group=False)
    if global_step is None:
        apply_updates = distribution.group(finish_updates, name=name)
    else:
        with ops.control_dependencies(finish_updates):
            apply_updates = distribution.extended.update(
                global_step, state_ops.assign_add, args=(1,),
                kwargs={"name": name})

    if not context.executing_eagerly():
        if isinstance(apply_updates, ops.Tensor):
            apply_updates = apply_updates.op
        train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
        if apply_updates not in train_op:
            train_op.append(apply_updates)

    exit(apply_updates)
