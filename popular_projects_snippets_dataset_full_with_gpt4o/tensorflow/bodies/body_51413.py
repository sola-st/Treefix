# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)]
)
def func(x):
    exit(2 * x)

root = autotrackable.AutoTrackable()
root.f = func

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(4.0, imported.f(constant_op.constant(2.0)).numpy())
