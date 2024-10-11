# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.path = asset.Asset(self._vocab_path)
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
root.get_asset = def_function.function(lambda: root.path.asset_path)
save.save(root, save_dir, signatures=root.get_asset.get_concrete_function())
second_dir = os.path.join(self.get_temp_dir(), "second_dir")
file_io.rename(save_dir, second_dir)
imported_path = _import_and_infer(second_dir, {})["output_0"]
self.assertIn(
    compat.as_str_any(second_dir), compat.as_str_any(imported_path))
