# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Apply gradients to variables.

    This is the second part of `minimize()`. It returns an `Operation` that
    applies gradients.

    @compatibility(TF2)
    #### How to Map Arguments

    | TF1 Arg Name          | TF2 Arg Name    | Note                       |
    | :-------------------- | :-------------- | :------------------------- |
    | `grads_and_vars`      | `grads_and_vars`| -                          |
    | `global_step`         | Not supported.  | Use `optimizer.iterations` |
    | `name`                | `name. `        | -                          |

    Args:
      grads_and_vars: List of (gradient, variable) pairs as returned by
        `compute_gradients()`.
      global_step: Optional `Variable` to increment by one after the
        variables have been updated.
      name: Optional name for the returned operation.  Default to the
        name passed to the `Optimizer` constructor.

    Returns:
      An `Operation` that applies the specified gradients. If `global_step`
      was not None, that operation also increments `global_step`.

    Raises:
      TypeError: If `grads_and_vars` is malformed.
      ValueError: If none of the variables have gradients.
      RuntimeError: If you should use `_distributed_apply()` instead.
    """
# This is a default implementation of apply_gradients() that can be shared
# by most optimizers.  It relies on the subclass implementing the following
# methods: _create_slots(), _prepare(), _apply_dense(), and _apply_sparse().

# TODO(isaprykin): Get rid of `has_strategy()` check by
# always calling _distributed_apply(), using the default distribution
# as needed.
if distribute_ctx.has_strategy():
    # Handle DistributionStrategy case.
    if distribute_ctx.in_cross_replica_context():
        raise RuntimeError("Use `_distributed_apply()` instead of "
                           "`apply_gradients()` in a cross-replica context.")

    grads_and_vars = get_filtered_grad_fn(lambda: grads_and_vars)()
    exit(distribute_ctx.get_replica_context().merge_call(
        self._distributed_apply, args=(grads_and_vars, global_step, name)))

# No DistributionStrategy case.
grads_and_vars = tuple(grads_and_vars)  # Make sure repeat iteration works.
if not grads_and_vars:
    raise ValueError("No variables provided.")
converted_grads_and_vars = []
for g, v in grads_and_vars:
    if g is not None:
        try:
            # Convert the grad to Tensor or IndexedSlices if necessary.
            g = ops.convert_to_tensor_or_indexed_slices(g)
        except TypeError:
            raise TypeError(
                "Gradient must be convertible to a Tensor"
                " or IndexedSlices, or None: %s" % g)
        if not isinstance(g, (ops.Tensor, indexed_slices.IndexedSlices)):
            raise TypeError(
                "Gradient must be a Tensor, IndexedSlices, or None: %s" % g)
    p = _get_processor(v)
    converted_grads_and_vars.append((g, v, p))

converted_grads_and_vars = tuple(converted_grads_and_vars)
var_list = [v for g, v, _ in converted_grads_and_vars if g is not None]
if not var_list:
    raise ValueError("No gradients provided for any variable: %s." %
                     ([str(v) for _, v, _ in converted_grads_and_vars],))
with ops.init_scope():
    self._create_slots(var_list)
update_ops = []
with ops.name_scope(name, self._name, skip_on_eager=False) as name:
    self._prepare()
    for grad, var, processor in converted_grads_and_vars:
        if grad is None:
            continue
        # We colocate all ops created in _apply_dense or _apply_sparse
        # on the same device as the variable.
        # TODO(apassos): figure out how to get the variable name here.
        if (context.executing_eagerly() or
            resource_variable_ops.is_resource_variable(var)
            and not var._in_graph_mode):  # pylint: disable=protected-access
            scope_name = ""
        else:
            scope_name = var.op.name
        with ops.name_scope(
            "update_" + scope_name,
            skip_on_eager=False), ops.colocate_with(var):
            update_ops.append(processor.update_op(self, grad))
    if global_step is None:
        apply_updates = self._finish(update_ops, name)
    else:
        with ops.control_dependencies([self._finish(update_ops, "update")]):
            with ops.colocate_with(global_step):
                if isinstance(
                    global_step, resource_variable_ops.BaseResourceVariable):
                    # TODO(apassos): the implicit read in assign_add is slow; consider
                    # making it less so.
                    apply_updates = resource_variable_ops.assign_add_variable_op(
                        global_step.handle,
                        ops.convert_to_tensor(1, dtype=global_step.dtype),
                        name=name)
                else:
                    apply_updates = state_ops.assign_add(global_step, 1, name=name)

    if not context.executing_eagerly():
        if isinstance(apply_updates, ops.Tensor):
            apply_updates = apply_updates.op
        train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
        if apply_updates not in train_op:
            train_op.append(apply_updates)

    exit(apply_updates)
