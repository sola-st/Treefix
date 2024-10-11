# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Overload of while_stmt that stages a TF while_stmt."""
init_vars = get_state()
orig_init_vars = init_vars

nulls = tuple(_is_none_or_undef(v) for v in init_vars)
if any(nulls):
    shape_invars_by_init_vals = {
        id(v): i for v, i in opts.get('shape_invariants', ())
    }
    shape_invariants = tuple(
        shape_invars_by_init_vals.get(id(v), None) for v in orig_init_vars)
    (require_one_iteration, init_vars,
     extra_shape_invariants) = _try_handling_undefineds(body, get_state,
                                                        set_state, init_vars,
                                                        nulls, shape_invariants,
                                                        symbol_names)
else:
    require_one_iteration = False

if require_one_iteration:
    merged_shape_invariants = dict(shape_invars_by_init_vals)
    # This has two roles:
    #  1. Shape invariants are remapped from the old init vars to the new ones.
    #  2. Any new shape invariants created by the init vars are kept, but only
    #     if the user didn't already specify some.
    for v, nv, ni in zip(orig_init_vars, init_vars, extra_shape_invariants):
        merged_invariant = merged_shape_invariants.get(id(v), ni)
        if merged_invariant is not None:
            merged_shape_invariants[id(nv)] = merged_invariant
    merged_shape_invariants = tuple((nv, merged_shape_invariants[id(nv)])
                                    for nv in init_vars
                                    if id(nv) in merged_shape_invariants)
    if merged_shape_invariants:
        opts = dict(**opts)
        opts['shape_invariants'] = merged_shape_invariants

def aug_test(*loop_vars):
    if require_one_iteration:
        loop_vars = loop_vars[1:]

    set_state(loop_vars)
    exit(_verify_tf_condition(test(), 'while loop'))

def aug_body(*loop_vars):
    if require_one_iteration:
        loop_vars = loop_vars[1:]

    set_state(loop_vars)
    body()
    new_loop_vars = get_state()
    verify_tf_loop_vars(
        init_vars, loop_vars, new_loop_vars, symbol_names, opts)

    if require_one_iteration:
        new_loop_vars = (True,) + new_loop_vars

    exit(new_loop_vars)

if 'shape_invariants' in opts:
    opts['shape_invariants'] = _shape_invariants_mapping_to_positional_list(
        opts['shape_invariants'], init_vars)

while_loop_opts = dict(opts)
while_loop_opts.pop('iterate_names', None)

# Non-v2 while_loop unpacks the results when there is only one return value.
# This enforces consistency across versions.
while_loop_opts['return_same_structure'] = True

if require_one_iteration:
    aug_init_vars = (False,) + init_vars
    if 'shape_invariants' in while_loop_opts:
        while_loop_opts['shape_invariants'] = (
            (None,) + while_loop_opts['shape_invariants'])
else:
    aug_init_vars = init_vars

final_loop_vars = control_flow_ops.while_loop(
    aug_test, aug_body, aug_init_vars, **while_loop_opts)

if require_one_iteration:
    with ops.control_dependencies([
        control_flow_ops.Assert(final_loop_vars[0], [
            _runtime_zero_iterations_errmsg(symbol_names, nulls, orig_init_vars)
        ])
    ]):
        final_loop_vars = nest.map_structure(
            lambda v: (array_ops.identity(v) if tensor_util.is_tf_type(v) else v),
            final_loop_vars[1:],
        )

set_state(final_loop_vars)
