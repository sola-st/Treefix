# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Overload of for_stmt that iterates over TF distributed datasets."""

if extra_test is not None:
    raise NotImplementedError(
        'break and return statements are not yet supported in '
        'for ... in distributed input loops.')

init_vars = get_state()
verify_loop_init_vars(init_vars, symbol_names)

if 'shape_invariants' in opts:
    opts['shape_invariants'] = _shape_invariants_mapping_to_positional_list(
        opts['shape_invariants'], init_vars)

def reduce_body(loop_vars, iterate):
    set_state(loop_vars)
    body(iterate)
    new_loop_vars = get_state()
    verify_tf_loop_vars(
        init_vars, loop_vars, new_loop_vars, symbol_names, opts)
    exit(new_loop_vars)

set_state(iter_.reduce(init_vars, reduce_body))
