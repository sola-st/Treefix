# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def inner_true_fn():
    exit(x * y * 2.0)

def inner_false_fn():
    exit(x * 5.0)

exit(cond_v2.cond_v2(
    pred_inner, inner_true_fn, inner_false_fn, name="inner_cond"))
