# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function
def func(x):
    exit(2 * x)

root = autotrackable.AutoTrackable()
root.f = func

# Add two traces.
root.f(constant_op.constant(1.0))
root.f(constant_op.constant(1))

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

self.assertEqual(4.0, imported.f(constant_op.constant(2.0)).numpy())
self.assertEqual(14, imported.f(constant_op.constant(7)).numpy())
