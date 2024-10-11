# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/critical_section_ops.py
"""Execute function `fn()` inside the critical section.

    `fn` should not accept any arguments.  To add extra arguments to when
    calling `fn` in the critical section, create a lambda:

    ```python
    critical_section.execute(lambda: fn(*my_args, **my_kwargs))
    ```

    Args:
      fn: The function to execute.  Must return at least one tensor.
      exclusive_resource_access: Whether the resources required by
        `fn` should be exclusive to this `CriticalSection`.  Default: `True`.
        You may want to set this to `False` if you will be accessing a
        resource in read-only mode in two different CriticalSections.
      name: The name to use when creating the execute operation.

    Returns:
      The tensors returned from `fn()`.

    Raises:
      ValueError: If `fn` attempts to lock this `CriticalSection` in any nested
        or lazy way that may cause a deadlock.
      ValueError: If `exclusive_resource_access == True` and
        another `CriticalSection` has an execution requesting the same
        resources as `fn``.  Note, even if `exclusive_resource_access` is
        `True`, if another execution in another `CriticalSection` was created
        without `exclusive_resource_access=True`, a `ValueError` will be raised.
    """
with ops.name_scope(name, "critical_section_execute", []):
    # Ensure that mutex locking only happens *after* all args and
    # kwargs have been executed.  This avoids certain types of deadlocks.
    with _push_critical_section_stack(self._signature):
        lock = gen_resource_variable_ops.mutex_lock(self._handle)

        if not context.executing_eagerly():
            # NOTE(ebrevdo): This is to ensure we don't pick up spurious
            # Operations created by other threads.
            with ops.get_default_graph()._lock:  # pylint: disable=protected-access
                existing_ops = ops.get_default_graph().get_operations()
                with ops.control_dependencies([lock]):
                    r = fn()
                # TODO(ebrevdo): If creating critical sections in a python loop,
                # this makes graph creation time quadratic.  Revisit if this
                # becomes a problem.
                created_ops = (set(ops.get_default_graph().get_operations())
                               .difference(existing_ops))
        else:
            with ops.control_dependencies([lock]):
                r = fn()

    if not context.executing_eagerly():
        self._add_control_dependencies_to_lock(created_ops, lock.op)

        # captured_resources is a list of resources that are directly
        # accessed only by ops created during fn(), not by any
        # ancestors of those ops in the graph.
        captured_resources = object_identity.ObjectIdentitySet([
            input_ for op in created_ops
            for input_ in op.inputs
            if input_.dtype == dtypes.resource
        ])

        # NOTE(ebrevdo): The only time self._is_self_handle() is True
        # in this call is if one of the recently created ops, within
        # the execute(), themselves attempt to access the
        # CriticalSection.  This will cause a deadlock.
        if any(self._is_self_handle(x) for x in captured_resources):
            raise ValueError(
                "Attempting to lock a CriticalSection in which we are "
                f"already running (signature={self._signature}). This is illegal "
                "and may cause deadlocks.")

        self._check_multiple_access_to_resources(
            captured_resources, exclusive_resource_access)

    r_flat = [_identity(x) for x in nest.flatten(r)]

    with ops.control_dependencies(r_flat):
        # The identity must run on the same machine as self._handle
        with ops.colocate_with(self._handle):
            # Do not use array_ops.identity as there are special
            # optimizations within TensorFlow which seem to elide it
            # even when optimizations are disabled(!).
            ensure_lock_exists = gen_resource_variable_ops.consume_mutex_lock(
                lock)

        # Make sure that if any element of r is accessed, all of
        # them are executed together.
        r = nest.pack_sequence_as(r, control_flow_ops.tuple(nest.flatten(r)))

    with ops.control_dependencies([ensure_lock_exists]):
        outputs = nest.map_structure(_identity, r)

    if not context.executing_eagerly():
        signature = _ExecutionSignature(
            op=lock.op,
            handle=self._handle,
            resources=list(captured_resources),
            exclusive_resource_access=exclusive_resource_access)
        ops.add_to_collections(
            CRITICAL_SECTION_EXECUTIONS, signature)

    exit(outputs)
