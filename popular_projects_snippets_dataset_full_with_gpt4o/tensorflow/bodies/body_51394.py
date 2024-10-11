# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
# Test 2 variables with same name: should work as the checkpoint
# is based on object name and not on variable name.
root.v1 = variables.Variable(1.0, trainable=True, name="v1")
root.v2 = variables.Variable(2.0, trainable=False, name="v1")
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(imported.v1.numpy(), 1.0)
self.assertEqual(imported.v2.numpy(), 2.0)
self.assertEqual(imported.v1.name, root.v1.name)
self.assertEqual(imported.v2.name, root.v2.name)
with variable_scope.variable_scope("foo"):
    imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
    self.assertTrue(imported.v1.name.startswith("foo/"))
    self.assertTrue(imported.v2.name.startswith("foo/"))
