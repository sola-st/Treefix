# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
set_state(init_vars)
orelse()
new_orelse_vars = get_state()
new_orelse_vars = new_orelse_vars[:nouts]
new_orelse_vars_[0] = new_orelse_vars
_verify_tf_cond_branch_vars(new_orelse_vars, symbol_names, 'else')
if new_body_vars_[0] is not None:
    _verify_tf_cond_vars(new_body_vars_[0], new_orelse_vars, symbol_names)
exit(new_orelse_vars)
