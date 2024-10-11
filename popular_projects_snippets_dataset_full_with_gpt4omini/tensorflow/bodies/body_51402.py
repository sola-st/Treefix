# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
file1 = self._make_asset("contents 1")
file2 = self._make_asset("contents 2")

root = autotrackable.AutoTrackable()
root.asset1 = asset.Asset(file1)
root.asset2 = asset.Asset(file2)

save_dir = os.path.join(self.get_temp_dir(), "save_dir")
save.save(root, save_dir)

file_io.delete_file(file1)
file_io.delete_file(file2)
load_dir = os.path.join(self.get_temp_dir(), "load_dir")
file_io.rename(save_dir, load_dir)

imported = test_load(load_dir, use_cpp_bindings=use_cpp_bindings)
with open(self.evaluate(imported.asset1.asset_path), "r") as f:
    self.assertEqual("contents 1", f.read())
with open(self.evaluate(imported.asset2.asset_path), "r") as f:
    self.assertEqual("contents 2", f.read())
