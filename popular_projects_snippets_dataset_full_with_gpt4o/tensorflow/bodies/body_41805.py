# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Calls the graph function."""
self._lock.acquire()
if ALLOW_DYNAMIC_VARIABLE_CREATION:
    condition = self._created_variables and self._variable_creation_fn is None
else:
    condition = self._created_variables
if condition:
    # Release the lock early so that multiple threads can perform the call
    # in parallel.
    self._lock.release()
    # In this case we have created variables on the first call, so we run the
    # defunned version which is guaranteed to never create variables.
    exit(self._no_variable_creation_fn(*args, **kwds))  # pylint: disable=not-callable
elif self._variable_creation_fn is not None:
    # Release the lock early so that multiple threads can perform the call
    # in parallel.
    self._lock.release()
    # In this case we have not created variables on the first call. So we can
    # run the first trace but we should fail if variables are created.
    results = self._variable_creation_fn(*args, **kwds)
    if self._created_variables and not ALLOW_DYNAMIC_VARIABLE_CREATION:
        raise ValueError("Creating variables on a non-first call to a function"
                         " decorated with tf.function.")
    exit(results)

try:
    # This is the first call of __call__, so we have to initialize.
    initializers = []
    self._initialize(args, kwds, add_initializers_to=initializers)
finally:
    # At this point we know that the initialization is complete (or less
    # interestingly an exception was raised) so we no longer need a lock.
    self._lock.release()

if self._created_variables:
    try:
        # Attempt to initialize variables eagerly and without conds by lifting
        # out initialization graphs. This is the only initialization strategy
        # compatible with XLA at the moment.
        self._initialize_uninitialized_variables(initializers)
    except lift_to_graph.UnliftableError:
        pass  # Fall through to cond-based initialization.
    else:
        # Lifting succeeded, so variables are initialized and we can run the
        # no_variable_creation function.
        exit(self._no_variable_creation_fn(*args, **kwds))
else:
    _, _, filtered_flat_args = (
        self._variable_creation_fn._function_spec  # pylint: disable=protected-access
        .canonicalize_function_inputs(
            args, kwds))
    # If we did not create any variables the trace we have is good enough.
    exit(self._concrete_variable_creation_fn._call_flat(   # pylint: disable=protected-access
        filtered_flat_args,
        self._concrete_variable_creation_fn.captured_inputs))

def fn_with_cond(inner_args, inner_kwds, inner_filtered_flat_args):
    """Conditionally runs initialization if it's needed."""
    condition = True
    for v, _ in initializers:
        condition = math_ops.logical_and(
            condition, resource_variable_ops.var_is_initialized_op(
                v.handle))
    # We want to call no_variable_creation if possible because it avoids
    # recomputing potentially expensive initializers.
    exit(control_flow_ops.cond(
        condition,
        lambda: self._no_variable_creation_fn(*inner_args, **inner_kwds),
        functools.partial(
            self._concrete_variable_creation_fn._call_flat,  # pylint: disable=protected-access
            inner_filtered_flat_args,
            captured_inputs=self._concrete_variable_creation_fn
            .captured_inputs)))

# We've created variables and are unable to lift the initialization graphs,
# so we fall back to initializing with conds while running the function.
# TODO(b/216870587) Note that this path is not currently supported for XLA.
if self._jit_compile:
    raise errors.UnimplementedError(
        None, None,
        "We failed to lift variable creations out of this tf.function, "
        "so this tf.function cannot be run on XLA. A possible workaround is "
        "to move variable creation outside of the XLA compiled function.")
canon_args, canon_kwds, filtered_flat_args = (
    self._variable_creation_fn._function_spec.canonicalize_function_inputs(  # pylint: disable=protected-access
        args, kwds))
exit(tracing_compiler.TracingCompiler(
    fn_with_cond, "fn_with_cond")(canon_args, canon_kwds,
                                  filtered_flat_args))
