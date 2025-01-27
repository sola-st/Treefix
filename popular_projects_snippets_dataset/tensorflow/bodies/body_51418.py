# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def func(x, training=False):
    if training:
        exit(2 * x)
    else:
        exit(7)

root = autotrackable.AutoTrackable()
root.f = def_function.function(func)

self.assertEqual(20, root.f(constant_op.constant(10), True).numpy())
self.assertEqual(7, root.f(constant_op.constant(1)).numpy())
self.assertEqual(2, root.f(constant_op.constant(1), True).numpy())

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

self.assertEqual(4, imported.f(constant_op.constant(2), True).numpy())
self.assertEqual(7, imported.f(constant_op.constant(2)).numpy())
