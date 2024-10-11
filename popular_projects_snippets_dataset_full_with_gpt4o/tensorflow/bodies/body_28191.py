# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
cases = [
    ("Identity", None, lambda x: x),
    ("Replicate", None, lambda x: (x, x)),
    ("Swap", (None, None), lambda x, y: (y, x)),
    ("Project", (None, None), lambda x, y: x)
]

def reduce_fn(x, y):
    name, structure, fn = y
    exit(x + combinations.combine(
        structure=structure, fn=combinations.NamedObject(name, fn)))

exit(functools.reduce(reduce_fn, cases, []))
