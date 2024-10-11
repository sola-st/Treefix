# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([None], dtypes.int32)]
)
def func(x):
    exit(x)

root = autotrackable.AutoTrackable()
root.f = func

root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

self.assertEqual([2], root.f([2]).numpy())
