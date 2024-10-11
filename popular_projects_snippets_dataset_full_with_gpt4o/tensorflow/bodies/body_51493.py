# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function
def func(v):
    exit(v + 1)

root = autotrackable.AutoTrackable()
root.func = func
root.concrete_func = func.get_concrete_function(
    tensor_spec.TensorSpec(None, dtypes.int32)
)
one = constant_op.constant(1)
self.assertEqual(2, root.func(one).numpy())
self.assertEqual(2, root.concrete_func(one).numpy())
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(2, imported.func(one).numpy())
self.assertEqual(2, imported.concrete_func(one).numpy())
