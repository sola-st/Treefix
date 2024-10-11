# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class M1(autotrackable.AutoTrackable):

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)]
    )
    def __call__(self, x):
        exit(x)

root = autotrackable.AutoTrackable()
root.m1 = M1()
root.m2 = autotrackable.AutoTrackable()
root.m2.__call__ = def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)]
)(lambda x: x * 3.0)
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
x = constant_op.constant(1.0)

self.assertTrue(callable(imported.m1))
self.assertAllEqual(root.m1(x), imported.m1(x))

# Note: `root.m2` was not callable since `__call__` attribute was set
# into the instance and not on the class. But after a serialization cycle
# that starts to work.
self.assertTrue(callable(imported.m2))
self.assertAllEqual(root.m2.__call__(x), imported.m2(x))

# Verify that user objects without `__call__` attribute are not callable.
self.assertFalse(callable(imported))
