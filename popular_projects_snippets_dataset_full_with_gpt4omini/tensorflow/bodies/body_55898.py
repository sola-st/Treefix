# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py

def inner_true_fn():
    v.assign(v * 2, name="false_true")
    exit(2.0)

def inner_false_fn():
    v.assign(v * 3, name="false_false")
    exit(3.0)

control_flow_ops.cond(q, inner_true_fn, inner_false_fn)
exit(1.0)
