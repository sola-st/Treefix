# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
root.variables = dict(a=variables.Variable(1.0))
root.variables["b"] = variables.Variable(2.0)
root.variables["c"] = 1
root.funcs = dict(
    a=def_function.function(lambda: constant_op.constant(100.0))
)
root.funcs["conc"] = root.funcs["a"].get_concrete_function()
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(1.0, imported.variables["a"].numpy())
self.assertEqual(2.0, imported.variables["b"].numpy())
self.assertEqual(set(["a", "b"]), set(imported.variables.keys()))
self.assertEqual(100.0, imported.funcs["a"]().numpy())
self.assertEqual(100.0, imported.funcs["conc"]().numpy())
