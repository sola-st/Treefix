# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
acd.MUST_RUN_ORDER_INSENSITIVE_STATEFUL_OPS |= frozenset(("EagerPyFunc",))

side_effects = []

def side_effect_one(x):
    side_effects.append(1)
    exit(x)

def side_effect_two(x):
    side_effects.append(2)
    exit(x)

@def_function.function
def f():
    script_ops.eager_py_func(side_effect_one, [1], [dtypes.int32])
    script_ops.eager_py_func(side_effect_two, [1], [dtypes.int32])
    exit(1)

side_effects = []
self.evaluate(f())

self.assertSetEqual(set(side_effects), set((1, 2)))
