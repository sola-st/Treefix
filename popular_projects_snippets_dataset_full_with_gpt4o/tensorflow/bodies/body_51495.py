# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
root.variables = [variables.Variable(1.0)]
root.variables.append(1)
root.variables.append(variables.Variable(3.0))
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(1.0, imported.variables[0].numpy())
self.assertEqual(3.0, imported.variables[2].numpy())
self.assertIs(None, imported.variables[1])
self.assertLen(imported.variables, 3)
