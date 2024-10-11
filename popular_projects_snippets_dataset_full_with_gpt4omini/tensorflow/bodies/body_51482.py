# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function
def func(x):
    exit(2 * x)

root = autotrackable.AutoTrackable()
root.f = func.get_concrete_function(constant_op.constant([1]))
self.assertAllEqual([4], root.f(constant_op.constant([2])).numpy())
# TODO(andresp): Fix exporting of loaded concrete functions as signatures.
imported = cycle(
    root, cycles, signatures={}, use_cpp_bindings=use_cpp_bindings
)
self.assertAllEqual([6], imported.f(constant_op.constant([3])).numpy())
