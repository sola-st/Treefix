# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def multiply():
    exit(x * 2)

def divide():
    exit(x // 2)

def defaults_two():
    exit(control_flow_ops.cond(
        math_ops.equal(math_ops.mod(x, 2), 0),
        multiply,
        divide,
        name="cond_mult"))

pred_fn_pairs = [
    (math_ops.logical_or(math_ops.equal(y, 2),
                         math_ops.equal(y, 3)), defaults_two),
]

exit(control_flow_ops.case(
    pred_fn_pairs, default=multiply, exclusive=True))
