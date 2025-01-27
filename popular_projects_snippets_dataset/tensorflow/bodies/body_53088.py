# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
exit(control_flow_ops.cond(
    b, true_fn=lambda: true_fn(x), false_fn=lambda: false_fn(x)))
