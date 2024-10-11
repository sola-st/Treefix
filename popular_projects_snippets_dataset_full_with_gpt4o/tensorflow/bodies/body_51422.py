# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function
def func(x, y):
    exit(string_ops.string_join([x, y]))

root = autotrackable.AutoTrackable()
root.f = func

self.assertAllEqual(b"ab", root.f("a", "b"))
self.assertAllEqual(b"ab", root.f("a", constant_op.constant("b")))
self.assertAllEqual(b"ab", root.f(constant_op.constant("a"), "b"))

concrete_functions = root.f._list_all_concrete_functions_for_serialization()  # pylint: disable=protected-access
self.assertLen(concrete_functions, 3)

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

self.assertAllEqual(b"ab", imported.f("a", "b"))
self.assertAllEqual(b"ab", imported.f("a", constant_op.constant("b")))
self.assertAllEqual(b"ab", imported.f(constant_op.constant("a"), "b"))
