# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
vocab = self._make_asset("contents")
root = autotrackable.AutoTrackable()
root.asset1 = asset.Asset(vocab)
root.asset2 = asset.Asset(vocab)
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(
    imported.asset1.asset_path.numpy(), imported.asset2.asset_path.numpy()
)
