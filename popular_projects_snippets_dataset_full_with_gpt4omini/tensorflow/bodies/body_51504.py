# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
exported = autotrackable.AutoTrackable()
exported.f = def_function.function(lambda: constant_op.constant(1.0))
imported = cycle(
    exported,
    cycles,
    signatures={"key": exported.f.get_concrete_function()},
    use_cpp_bindings=use_cpp_bindings,
)
self.assertEqual(1.0, imported.signatures["key"]()["output_0"].numpy())
imported.signatures = {"key1": imported.signatures["key"]}
with self.assertRaisesRegex(ValueError, "signatures"):
    save.save(imported, tempfile.mkdtemp(prefix=self.get_temp_dir()))
