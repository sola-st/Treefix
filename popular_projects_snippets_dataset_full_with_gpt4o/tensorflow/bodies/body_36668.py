# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def false_true_true_fn():
    exit(x * y * 2.0)

def false_true_false_fn():
    exit(x * 10.0)

exit(_cond(
    pred1,
    false_true_true_fn,
    false_true_false_fn,
    name="inside_false_true_fn"))
