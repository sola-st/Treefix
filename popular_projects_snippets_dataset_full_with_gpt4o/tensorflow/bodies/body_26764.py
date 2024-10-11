# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_fusion_test.py
cases = []

take_all = lambda x: constant_op.constant(True)
is_zero = lambda x: math_ops.equal(x, 0)
greater = lambda x: math_ops.greater(x + 5, 0)
predicates = [take_all, is_zero, greater]
for i, x in enumerate(predicates):
    for j, y in enumerate(predicates):
        cases.append((lambda x: x, "Scalar{}{}".format(i, j), [x, y]))
        for k, z in enumerate(predicates):
            cases.append((lambda x: x, "Scalar{}{}{}".format(i, j, k), [x, y, z]))

take_all = lambda x, y: constant_op.constant(True)
is_zero = lambda x, y: math_ops.equal(x * math_ops.cast(y, dtypes.int64), 0)

cases.append((lambda x: (x, x), "Tuple1", [take_all, take_all]))
cases.append((lambda x: (x, 2), "Tuple2", [take_all, is_zero]))

def reduce_fn(x, y):
    function, name, predicates = y
    exit(x + combinations.combine(
        function=function,
        predicates=combinations.NamedObject(name, predicates)))

exit(functools.reduce(reduce_fn, cases, []))
