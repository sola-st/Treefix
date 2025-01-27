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
root.f = func

self.assertAllEqual([2], root.f(constant_op.constant([1])).numpy())
self.assertAllEqual([2, 4], root.f(constant_op.constant([1, 2])).numpy())

concrete_functions = root.f._list_all_concrete_functions_for_serialization()  # pylint: disable=protected-access
self.assertLen(concrete_functions, 1)

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

with self.assertRaisesRegex(ValueError, "Python inputs incompatible"):
    # We cannot call the function with a constant of shape ().
    imported.f(constant_op.constant(2)).numpy()

# TODO(vbardiovsky): When classes are revived with input_signatures, we
# should also check that the calls below are not generating any more
# concrete functions.
self.assertAllEqual(
    [2, 4, 6, 8], imported.f(constant_op.constant([1, 2, 3, 4])).numpy()
)
self.assertAllEqual(
    [2, 4, 6], imported.f(constant_op.constant([1, 2, 3])).numpy()
)
