# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
if require_one_iteration:
    loop_vars = loop_vars[1:]

set_state(loop_vars)
exit(_verify_tf_condition(test(), 'while loop'))
