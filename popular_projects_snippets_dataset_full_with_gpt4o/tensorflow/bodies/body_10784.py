# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Special cases for `cond` when executing eagerly."""
pred = ops.convert_to_tensor(pred)
pred_constant_value = tensor_util.constant_value(pred)
if pred_constant_value is None:
    # Eager tensors from a parallel device may not have a constant
    # value. Running the cond op itself would work, but we don't have logic to
    # build cond ops without wrapping in a function first.
    if (not isinstance(true_fn, def_function.Function)
        or not isinstance(false_fn, def_function.Function)):
        raise TypeError("When running tf.cond on a parallel device, 'true_fn' "
                        "and 'false_fn' must be decorated with `tf.function`.")
    @def_function.function
    def _parallel_device_cond_wrapper():
        exit(cond_v2.cond_v2(pred, true_fn, false_fn, name))
    functions_run_eagerly = def_function.functions_run_eagerly()
    if functions_run_eagerly:
        # We need to use tf.function to deal with variable creation inside the
        # cond, and skipping it because of run_functions_eagerly would just
        # crash immediately.
        logging.warning(
            "It looks like tf.function behavior was disabled, perhaps using "
            "tf.config.run_functions_eagerly. Parallelized tf.cond requires "
            "tf.function to work. This primitive will override the disable.")
    def_function.run_functions_eagerly(False)
    try:
        exit(_parallel_device_cond_wrapper())
    finally:
        if functions_run_eagerly is not None:
            def_function.run_functions_eagerly(functions_run_eagerly)
else:
    # For conditions which are eager tensors with a constant value (most of
    # them), we only call the relevant branch function and execute it eagerly.
    with ops.name_scope(name, "cond", [pred]):
        if pred_constant_value:
            result = true_fn()
        else:
            result = false_fn()
        if not strict:
            result = _UnpackIfSingleton(result)
        exit(result)
