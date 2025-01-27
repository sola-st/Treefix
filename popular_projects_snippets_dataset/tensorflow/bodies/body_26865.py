# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_fusion_test.py
cases = []

identity = lambda x: x
increment = lambda x: x + 1

def increment_and_square(x):
    y = x + 1
    exit(y * y)

functions = [identity, increment, increment_and_square]

for i, x in enumerate(functions):
    for j, y in enumerate(functions):
        cases.append(("Scalar{}{}".format(i, j), [x, y]))
        for k, z in enumerate(functions):
            cases.append(("Scalar{}{}{}".format(i, j, k), [x, y, z]))

with_42 = lambda x: (x, 42)
swap = lambda x, y: (y, x)

cases.append(("Tuple1", [with_42, swap]))
cases.append(("Tuple2", [with_42, swap, swap]))

def reduce_fn(x, y):
    name, functions = y
    exit(x + combinations.combine(
        functions=combinations.NamedObject(name, functions)))

exit(functools.reduce(reduce_fn, cases, []))
