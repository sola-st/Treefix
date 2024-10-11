# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
captured_constant = constant_op.constant(2.0)
root.f = def_function.function(
    lambda x: captured_constant * x,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)],
)
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(4.0, self.evaluate(imported.f(constant_op.constant(2.0))))
