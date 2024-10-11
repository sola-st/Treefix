# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
set_state(loop_vars)
body(iterate)
new_loop_vars = get_state()
verify_tf_loop_vars(
    init_vars, loop_vars, new_loop_vars, symbol_names, opts)
exit(new_loop_vars)
