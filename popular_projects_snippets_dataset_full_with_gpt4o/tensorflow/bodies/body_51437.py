# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def func(x, training=False, **options):
    del options
    if training:
        exit(2 * x)
    else:
        exit(7)

root = autotrackable.AutoTrackable()
root.f = def_function.function(func)

x = constant_op.constant(10)
self.assertEqual(7, root.f(x, learning_rate=0.5, epochs=3).numpy())

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

with self.assertRaisesRegex(
    ValueError, "Could not find matching concrete function to call.*"
):
    imported.f(x, learning_rate=0.5, epochs=4)

self.assertEqual(7, imported.f(x, learning_rate=0.5, epochs=3).numpy())
