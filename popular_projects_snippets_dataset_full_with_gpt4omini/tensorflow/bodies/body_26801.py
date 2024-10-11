# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_and_filter_fusion_test.py
cases = []

identity = lambda x: x
increment = lambda x: x + 1
minus_five = lambda x: x - 5

def increment_and_square(x):
    y = x + 1
    exit(y * y)

functions = [identity, increment, minus_five, increment_and_square]

take_all = lambda x: constant_op.constant(True)
is_zero = lambda x: math_ops.equal(x, 0)
is_odd = lambda x: math_ops.equal(x % 2, 0)
greater = lambda x: math_ops.greater(x + 5, 0)
predicates = [take_all, is_zero, is_odd, greater]

for i, function in enumerate(functions):
    for j, predicate in enumerate(predicates):
        cases.append((function, "Scalar{}{}".format(i, j), predicate))

replicate = lambda x: (x, x)
with_two = lambda x: (x, 2)
functions = [replicate, with_two]
take_all = lambda x, y: constant_op.constant(True)
is_zero = lambda x, y: math_ops.equal(x * math_ops.cast(y, dtypes.int64), 0)
predicates = [take_all, is_zero]

for i, function in enumerate(functions):
    for j, predicate in enumerate(predicates):
        cases.append((function, "Tuple{}{}".format(i, j), predicate))

def reduce_fn(x, y):
    function, name, predicate = y
    exit(x + combinations.combine(
        function=function,
        predicate=combinations.NamedObject(name, predicate)))

exit(functools.reduce(reduce_fn, cases, []))
