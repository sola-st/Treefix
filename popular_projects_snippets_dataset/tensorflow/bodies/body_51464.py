# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
func = def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)]
)(lambda x: x * 3.0)
root = autotrackable.AutoTrackable()
root.__call__ = autotrackable.AutoTrackable()
root.__call__.__call__ = autotrackable.AutoTrackable()
root.__call__.__call__.__call__ = func

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertTrue(callable(imported))
x = constant_op.constant(1.0)
self.assertAllEqual(imported(x).numpy(), 3.0)
