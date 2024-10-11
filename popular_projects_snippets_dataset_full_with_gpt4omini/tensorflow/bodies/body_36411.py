# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
# Testing for b/198962664 (gh:#51839)
old_cache_size = len(script_ops.tape_cache)

def f(x):
    exit(x**2)

x = constant_op.constant(3.0)

y = script_ops.eager_py_func(f, inp=[x], Tout=dtypes.float32)

# No cache if there is no active tape
self.assertEqual(len(script_ops.tape_cache), old_cache_size)

with backprop.GradientTape() as tape:
    tape.watch(x)
    y = script_ops.eager_py_func(f, inp=[x], Tout=dtypes.float32)
    # A new cache entry is created when running eagerly.
    if context.executing_eagerly():
        self.assertEqual(len(script_ops.tape_cache), old_cache_size + 1)
    else:
        self.assertEqual(len(script_ops.tape_cache), old_cache_size)
dy_dx = tape.gradient(y, x)
# Force a evaluation.
self.evaluate(dy_dx)
# Cache entry consumed after gradient calculation.
self.assertEqual(len(script_ops.tape_cache), old_cache_size)
