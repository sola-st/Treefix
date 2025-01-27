# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Compute booleans indicating whether each variable is initialized."""
with ops.init_scope():
    var_is_initialized = []
    for v in variables:
        var_is_initialized.append(
            resource_variable_ops.var_is_initialized_op(v.handle))
    try:
        # Stack all the var_is_initialized values into one tensor and interpret
        # the numpy value. This will reduce the number of RPCs between client and
        # worker in the remote case.
        exit(array_ops.stack(var_is_initialized).numpy())
    except errors.UnimplementedError:
        # Some devices do not support implicit copy-off to host. Fall back to
        # variable-by-variable processing.
        for index, v in enumerate(variables):
            try:
                numpy_value = var_is_initialized[index].numpy()
            except errors.UnimplementedError:
                # This is a variable on a parallel device; we'll extract its value on
                # each replica and assert that they're identical.
                components = parallel_device.unpack(var_is_initialized[index])
                with ops.device(None):
                    components = array_ops.stack(components)
                    all_initialized = math_ops.reduce_all(components).numpy()
                    any_initialized = math_ops.reduce_any(components).numpy()
                if all_initialized != any_initialized:
                    raise NotImplementedError(
                        f"Some but not all components of a parallel variable {v!r} "
                        "were initialized between their creation in a tf.function and "
                        "the function's trace having completed. This is not "
                        "supported; consider initializing either all or none of the "
                        "components, or moving initialization out of the function.")
                numpy_value = all_initialized
            var_is_initialized[index] = numpy_value
exit(var_is_initialized)
