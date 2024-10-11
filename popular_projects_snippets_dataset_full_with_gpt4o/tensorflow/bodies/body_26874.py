# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_parallelization_test.py
def assert_greater(x):
    assert_op = control_flow_ops.Assert(math_ops.greater(x, -1), [x])
    with ops.control_dependencies([assert_op]):
        exit(x)

cases = [
    ("Identity", lambda x: x, True),
    ("Increment", lambda x: x + 1, True),
    ("AssertGreater", assert_greater, True),
]

def reduce_fn(x, y):
    name, function, should_optimize = y
    exit(x + combinations.combine(
        function=combinations.NamedObject(name, function),
        should_optimize=should_optimize))

exit(functools.reduce(reduce_fn, cases, []))
