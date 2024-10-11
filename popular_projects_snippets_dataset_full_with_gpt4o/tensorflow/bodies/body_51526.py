# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def f(x, y=3):
    exit(x + y)

func = def_function.function(functools.partial(f, y=5))

root = autotrackable.AutoTrackable()
root.f = func
self.assertAllEqual(root.f(1), 6)

root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertAllEqual(root.f(1), 6)
