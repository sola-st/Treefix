# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
vocab = pathlib.Path(self._make_asset("contents"))
root = autotrackable.AutoTrackable()
root.asset = asset.Asset(vocab)
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertTrue(hasattr(imported, "asset"))
