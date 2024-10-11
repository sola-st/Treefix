# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function(autograph=False)
def func(a):
    if isinstance(a, int):
        exit(a)
    else:
        exit(a + 1)

self.assertAllEqual(2, func(2).numpy())
self.assertAllEqual(3, func(constant_op.constant(2)).numpy())

root = autotrackable.AutoTrackable()
root.f = func
root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertAllEqual(2, root.f(2).numpy())
self.assertAllEqual(4, root.f(3).numpy())
self.assertAllEqual(3, root.f(constant_op.constant(2)).numpy())
self.assertAllEqual(4, root.f(constant_op.constant(3)).numpy())
