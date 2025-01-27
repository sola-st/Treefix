# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
set_state(init_vars)
body()
new_body_vars = get_state()
new_body_vars = new_body_vars[:nouts]
new_body_vars_[0] = new_body_vars
_verify_tf_cond_branch_vars(new_body_vars, symbol_names, 'main')
if new_orelse_vars_[0] is not None:
    _verify_tf_cond_vars(new_body_vars, new_orelse_vars_[0], symbol_names)
exit(new_body_vars)
