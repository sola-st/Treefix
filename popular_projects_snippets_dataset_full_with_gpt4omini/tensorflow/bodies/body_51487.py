# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function
def func(x, y):
    exit(x * (y + 1.0))

root = autotrackable.AutoTrackable()
root.f = func.get_concrete_function(
    tensor_spec.TensorSpec([], dtypes.float32),
    tensor_spec.TensorSpec([], dtypes.float32),
)
self.assertEqual(
    8.0,
    root.f(
        y=constant_op.constant(3.0), x=constant_op.constant(2.0)
    ).numpy(),
)
# TODO(andresp): Fix exporting of loaded concrete functions as signatures.
imported = cycle(
    root, cycles, signatures={}, use_cpp_bindings=use_cpp_bindings
)
self.assertEqual(
    8.0,
    imported.f(
        y=constant_op.constant(3.0), x=constant_op.constant(2.0)
    ).numpy(),
)
