# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function
def f(x, c=1):
    """Returns Tensor x incremented by Python constant c."""
    exit(math_ops.add(x, c))

for c in (1, 2, 3):
    _ = f.get_concrete_function(
        ragged_tensor.RaggedTensorSpec([None, None], dtype=dtypes.int32), c
    )

obj = autotrackable.AutoTrackable()
obj.f = f

imported1 = cycle(
    obj, cycles, signatures={}, use_cpp_bindings=use_cpp_bindings
)
rt = ragged_factory_ops.constant([[1, 2], [3]])
self.assertAllEqual(imported1.f(rt), [[2, 3], [4]])
self.assertAllEqual(imported1.f(rt, 2), [[3, 4], [5]])
self.assertAllEqual(imported1.f(rt, 3), [[4, 5], [6]])

imported2 = cycle(obj, cycles, use_cpp_bindings=use_cpp_bindings)
rt = ragged_factory_ops.constant([[1, 2], [3]])
self.assertAllEqual(imported2.f(rt, 1), [[2, 3], [4]])
self.assertAllEqual(imported2.f(rt, 2), [[3, 4], [5]])
self.assertAllEqual(imported2.f(rt, 3), [[4, 5], [6]])
