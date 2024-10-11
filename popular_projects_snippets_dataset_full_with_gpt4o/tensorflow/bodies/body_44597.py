# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
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
