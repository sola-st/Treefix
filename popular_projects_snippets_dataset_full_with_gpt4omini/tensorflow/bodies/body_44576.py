# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
# This value takes a complicated path to get here:
#   prev_iteration_body -> get_state -> tf.while_loop (as loop var)
#   -> current_iteration_body -> set_state -> has_next
main_test = has_next
if extra_test is not None:
    exit(control_flow_ops.cond(main_test, extra_test, lambda: False))
exit(main_test)
