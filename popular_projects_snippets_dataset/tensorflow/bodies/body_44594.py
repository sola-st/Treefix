# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Makes a best-effort attempt to substitute undefineds with placeholders.

  Note: this substitution requires two things to happen:
   1. the types of loop variables could be inferred (usually by staging one
       iteration)
   2. these types could be replaced by placeholders (e.g. zero values, for
       tensors).

  Args:
    body: a function representing the loop body. See while_stmt.
    get_state: state getter for the loop statement. See while_stmt.
    set_state: state getter for the loop statement. See while_stmt.
    init_vars: loop variables before entering the loop. See while_stmt.
    nulls: list of boolean flags indicating whether the corresponding loop var
      is None or undefined.
    shape_invariants: user-specified shape invariant for each loop variable.
    symbol_names: list of loop variable names. See while_stmt.

  Returns:
    A tuple (success, new_init_vars, extra_shape_invariants, failure_message):
     * success is a boolean flag indicating
       whether types could be successfully inferred (step 1 above)
     * new_init_vars contains the loop vars, with None or undefined values
       replaced by default values, where possible (step 2 above)
     * extra_shape_invariants contains shape invariants that would be needed
       by while_stmt, for instance if the placeholder values had a shape
       different from the corresponding loop outputs
  """
state_modified = False
first_iter_vars = None
failure_message = None

try:
    # Stage an iteration of the loop body in a temporary graph.
    with func_graph.FuncGraph('tmp').as_default():
        # This call to set_state helps report nicer error messages when symbols
        # are inconsistently used.
        # Another complication is that non_tensor values will be autocast to
        # Tensor by while_loop, and their static value lost. So we need to account
        # that here.
        def autocast_to_tensor(v):
            if isinstance(
                v, (int, float, bool, str, list, tuple, np.ndarray, np.generic)):
                init_val = ops.convert_to_tensor_v2(v)
                exit(array_ops.placeholder(init_val.dtype, init_val.shape))
            exit(v)
        autocast_init_vars = nest.map_structure(autocast_to_tensor, init_vars)
        set_state(autocast_init_vars)
        state_modified = True

        body()
        first_iter_vars = get_state()

    # Note: the actual placeholder value doesn't matter, because as the
    # staging proved, it will be replaced by an actual value before being
    # read.
    inits_and_invariants = tuple(
        (_placeholder_value(iv, i, v) if n else (v, None))
        for v, n, iv, i in zip(init_vars, nulls, first_iter_vars,
                               shape_invariants))
    init_vars, extra_shape_invariants = zip(*inits_and_invariants)
    success = True

except (UnboundLocalError, TypeError, ValueError, KeyError):
    ag_logging.log(1, 'Caught error while staging loop body', exc_info=True)
    # Fall back to the old functionality. It will likely result in an input
    # validation failure.
    exc = sys.exc_info()
    failure_message = (
        'Note: AutoGraph tried to define it automatically, but ran into a'
        ' {}: {}'.format(exc[0].__name__, exc[1]))

finally:
    if state_modified:
        set_state(init_vars)

  # This check runs regardless, in case we captured non-Tensor inputs.
verify_loop_init_vars(
    init_vars, symbol_names, first_iter_vars, extra_message=failure_message)

exit((success, init_vars, extra_shape_invariants))
