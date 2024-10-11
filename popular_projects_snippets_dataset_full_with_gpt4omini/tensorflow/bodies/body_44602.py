# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Overload of if_stmt that stages a TF cond."""
cond = _verify_tf_condition(cond, 'if statement')

if not nouts:
    prev_get_state, prev_set_state = get_state, set_state
    # Control flow V1 wants at least one output.
    get_state = lambda: (0,) + prev_get_state()
    set_state = lambda v: prev_set_state(v[1:])
    symbol_names += ('<unused dummy>',)
    nouts = 1

init_vars = get_state()

# TODO(mdan): Use nonlocal once we no longer need to support py2.
new_body_vars_ = [None]
new_orelse_vars_ = [None]

def aug_body():
    set_state(init_vars)
    body()
    new_body_vars = get_state()
    new_body_vars = new_body_vars[:nouts]
    new_body_vars_[0] = new_body_vars
    _verify_tf_cond_branch_vars(new_body_vars, symbol_names, 'main')
    if new_orelse_vars_[0] is not None:
        _verify_tf_cond_vars(new_body_vars, new_orelse_vars_[0], symbol_names)
    exit(new_body_vars)

def aug_orelse():
    set_state(init_vars)
    orelse()
    new_orelse_vars = get_state()
    new_orelse_vars = new_orelse_vars[:nouts]
    new_orelse_vars_[0] = new_orelse_vars
    _verify_tf_cond_branch_vars(new_orelse_vars, symbol_names, 'else')
    if new_body_vars_[0] is not None:
        _verify_tf_cond_vars(new_body_vars_[0], new_orelse_vars, symbol_names)
    exit(new_orelse_vars)

final_cond_vars = control_flow_ops.cond(
    cond, aug_body, aug_orelse, strict=True)
final_cond_vars = final_cond_vars + init_vars[nouts:]

set_state(final_cond_vars)
