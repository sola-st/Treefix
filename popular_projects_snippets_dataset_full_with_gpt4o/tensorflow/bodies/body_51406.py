# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
root.vocab = asset.Asset(self._make_asset("contents"))
root.f = def_function.function(
    lambda: root.vocab.asset_path, input_signature=[]
)
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
original_output = root.f().numpy()
imported_output = imported.f().numpy()
self.assertNotEqual(original_output, imported_output)
with open(imported_output, "r") as f:
    self.assertEqual("contents", f.read())
