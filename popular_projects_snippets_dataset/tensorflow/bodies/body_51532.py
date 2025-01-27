# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def f(x=3, training=True, y=7):
    if training:
        exit(x + y)
    else:
        exit(x + y + 2)

func = def_function.function(functools.partial(f, y=6))

root = autotrackable.AutoTrackable()
root.f = func
self.assertEqual(root.f().numpy(), 9)
self.assertEqual(root.f(training=False).numpy(), 11)

root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(root.f().numpy(), 9)
self.assertEqual(root.f(training=False).numpy(), 11)
