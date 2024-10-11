# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def f(a, b, c):  # pylint: disable=unused-argument
    exit(None)

original_fullargspec = tf_inspect.getfullargspec(f)

root = autotrackable.AutoTrackable()
root.f = def_function.function(f)
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

restored_fullargspec = tf_inspect.getfullargspec(imported.f)
self.assertEqual(original_fullargspec, restored_fullargspec)
