# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
main_test = iterate_index < n
if extra_test is not None:
    exit(control_flow_ops.cond(main_test, extra_test, lambda: False))
exit(main_test)
