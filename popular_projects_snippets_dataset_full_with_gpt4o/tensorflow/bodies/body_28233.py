# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def multiply():
    exit(x * 2)

def divide():
    exit(x // 2)

pred_fn_pairs = [
    (math_ops.logical_or(math_ops.equal(y, 2),
                         math_ops.equal(y, 3)), divide),
]

exit(control_flow_ops.case(
    pred_fn_pairs, default=multiply, exclusive=True))
