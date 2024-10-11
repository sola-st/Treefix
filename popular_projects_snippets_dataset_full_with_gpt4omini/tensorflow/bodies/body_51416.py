# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
f = def_function.function(
    lambda x: x * 2.0,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)],
)
g = def_function.function(
    lambda x: f(x) + 1.0,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)],
)

root = autotrackable.AutoTrackable()
root.g = g
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
imported.g(constant_op.constant([1.0]))
