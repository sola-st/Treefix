# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def func(x, dtype=None):
    if dtype:
        exit(array_ops.zeros(shape=x.shape, dtype=dtype))
    else:
        exit(array_ops.zeros(shape=x.shape, dtype=dtypes.float32))

root = autotrackable.AutoTrackable()
root.f = def_function.function(func)

self.assertAllEqual(
    [0.0, 0.0, 0.0], root.f(constant_op.constant([1, 2, 3])).numpy()
)
self.assertAllEqual(
    [0.0, 0.0, 0.0], root.f(constant_op.constant([1.0, 2.0, 3.0])).numpy()
)
self.assertAllEqual(
    [0.0, 0.0, 0.0, 0.0], root.f(constant_op.constant([1, 2, 3, 4])).numpy()
)
self.assertAllEqual(
    [0, 0, 0],
    root.f(
        constant_op.constant([1.0, 2.0, 3.0]), dtype=dtypes.int32
    ).numpy(),
)

concrete_functions = root.f._list_all_concrete_functions_for_serialization()  # pylint: disable=protected-access
self.assertLen(concrete_functions, 4)

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

self.assertAllEqual(
    [0.0, 0.0, 0.0],
    imported.f(constant_op.constant([1, 2, 3]), None).numpy(),
)
self.assertAllEqual(
    [0.0, 0.0, 0.0],
    imported.f(constant_op.constant([1.0, 2.0, 3.0])).numpy(),
)
self.assertAllEqual(
    [0.0, 0.0, 0.0, 0.0],
    imported.f(constant_op.constant([1, 2, 3, 4])).numpy(),
)
self.assertAllEqual(
    [0, 0, 0],
    imported.f(
        constant_op.constant([1.0, 2.0, 3.0]), dtype=dtypes.int32
    ).numpy(),
)
