# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function
def func(x, training=False):
    if training:
        exit(2 * x)
    else:
        exit(3 * x)

func.get_concrete_function(
    tensor_spec.TensorSpec([None], dtypes.int32), True
)
func.get_concrete_function(tensor_spec.TensorSpec([None], dtypes.float32))

root = autotrackable.AutoTrackable()
root.f = func

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

concrete = imported.f.get_concrete_function(
    training=True, x=tensor_spec.TensorSpec([None], dtypes.int32)
)

self.assertAllEqual(
    [2, 4, 6, 8], concrete(x=constant_op.constant([1, 2, 3, 4])).numpy()
)
with self.assertRaisesRegex(
    ValueError, "Could not find matching concrete function to call"
):
    imported.f.get_concrete_function(
        tensor_spec.TensorSpec([None], dtypes.int32)
    )
imported.f.get_concrete_function(
    tensor_spec.TensorSpec([None], dtypes.int32), True
)
