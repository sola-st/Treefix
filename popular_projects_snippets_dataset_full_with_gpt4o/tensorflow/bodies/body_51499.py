# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
const = array_ops.zeros([100])
root = autotrackable.AutoTrackable()
root.f = def_function.function(lambda: const + 1.0)
root.g = def_function.function(lambda: const + 2.0)
self.assertAllClose(array_ops.ones([100]), root.f())
self.assertAllClose(2.0 * array_ops.ones([100]), root.g())
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertAllClose(array_ops.ones([100]), imported.f())
self.assertAllClose(2.0 * array_ops.ones([100]), imported.g())
# TODO(b/123408994): Use the public get_concrete_function.
f_concrete = imported.f._list_all_concrete_functions_for_serialization()[0]
g_concrete = imported.g._list_all_concrete_functions_for_serialization()[0]
self.assertLen(f_concrete.captured_inputs, 1)
self.assertLen(g_concrete.captured_inputs, 1)
# We should be using the same captured EagerTensor in both functions, not
# duplicating the constant.
self.assertIs(f_concrete.captured_inputs[0], g_concrete.captured_inputs[0])
