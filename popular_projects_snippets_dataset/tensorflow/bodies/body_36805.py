# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
if _is_old_cond():
    exit(control_flow_ops.cond(pred, true_fn, false_fn, name=name))
else:
    exit(cond_v2.cond_v2(pred, true_fn, false_fn, name=name))
