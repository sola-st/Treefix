# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([None], dtypes.int32)]
)
def func(x):
    exit(2 * x)

root = autotrackable.AutoTrackable()
root.f = func.get_concrete_function()

self.assertAllEqual([2], root.f(constant_op.constant([1])).numpy())
self.assertAllEqual([2, 4], root.f(constant_op.constant([1, 2])).numpy())

# TODO(andresp): Fix exporting of loaded concrete functions as signatures.
imported = cycle(
    root, cycles, signatures={}, use_cpp_bindings=use_cpp_bindings
)

self.assertAllEqual(
    [2, 4, 6, 8], imported.f(constant_op.constant([1, 2, 3, 4])).numpy()
)
self.assertAllEqual(
    [2, 4, 6], imported.f(constant_op.constant([1, 2, 3])).numpy()
)
