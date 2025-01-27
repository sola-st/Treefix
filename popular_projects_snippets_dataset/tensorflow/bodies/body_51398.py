# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
root.weights = variables.Variable(2.0)
self.evaluate(root.weights.initializer)
root.f = def_function.function(
    lambda x: root.weights * x,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)],
)
for _ in range(cycles):
    imported = cycle(root, 1, use_cpp_bindings=use_cpp_bindings)
    self.evaluate(imported.weights.initializer)
self.assertEqual(4.0, self.evaluate(imported.f(constant_op.constant(2.0))))
self.evaluate(imported.weights.assign(4.0))
self.assertEqual(8.0, self.evaluate(imported.f(constant_op.constant(2.0))))
