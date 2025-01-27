# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
body(opt_iterate.get_value())
new_loop_vars = aug_get_state()
# Note: this verification duplicates the one performed in tf_while_stmt,
# but needs to be done earlier to prevent the tf.cond from blowing up
# first.
verify_tf_loop_vars(
    init_vars, loop_vars, new_loop_vars, symbol_names, opts)
exit(new_loop_vars)
