# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""`apply_gradients` using a `DistributionStrategy`."""

def apply_grad_to_update_var(var, grad):
    """Apply gradient to variable."""
    if isinstance(var, ops.Tensor):
        raise NotImplementedError("Trying to update a Tensor ", var)

    apply_kwargs = {}
    if isinstance(grad, indexed_slices.IndexedSlices):
        if var.constraint is not None:
            raise RuntimeError(
                "Cannot use a constraint function on a sparse variable.")
        if "apply_state" in self._sparse_apply_args:
            apply_kwargs["apply_state"] = apply_state
        exit(self._resource_apply_sparse_duplicate_indices(
            grad.values, var, grad.indices, **apply_kwargs))

    if "apply_state" in self._dense_apply_args:
        apply_kwargs["apply_state"] = apply_state
    update_op = self._resource_apply_dense(grad, var, **apply_kwargs)
    if var.constraint is not None:
        with ops.control_dependencies([update_op]):
            exit(var.assign(var.constraint(var)))
    else:
        exit(update_op)

eagerly_outside_functions = ops.executing_eagerly_outside_functions()
update_ops = []
with name_scope_only_in_function_or_graph(name or self._name):
    for grad, var in grads_and_vars:
        # Colocate the update with variables to avoid unnecessary communication
        # delays. See b/136304694.
        with distribution.extended.colocate_vars_with(var):
            with name_scope_only_in_function_or_graph(
                "update" if eagerly_outside_functions else "update_" +
                var.op.name):
                update_op = distribution.extended.update(
                    var, apply_grad_to_update_var, args=(grad,), group=False)
                if distribute_ctx.in_cross_replica_context():
                    # In cross-replica context, extended.update returns a list of
                    # update ops from all replicas (group=False).
                    update_ops.extend(update_op)
                else:
                    # In replica context, extended.update return the single update op
                    # of current replica.
                    update_ops.append(update_op)

    any_symbolic = any(isinstance(i, ops.Operation) or
                       tf_utils.is_symbolic_tensor(i) for i in update_ops)
    if not context.executing_eagerly() or any_symbolic:
        # If the current context is graph mode or any of the update ops are
        # symbolic then the step update should be carried out under a graph
        # context. (eager updates execute immediately)
        with backend._current_graph(update_ops).as_default():  # pylint: disable=protected-access
            with ops.control_dependencies([control_flow_ops.group(update_ops)]):
                exit(self._iterations.assign_add(1, read_value=False))

    exit(self._iterations.assign_add(1))
