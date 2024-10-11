# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
if use_cpp_bindings:
    self.skipTest("Cpp bindings cannot work with pathlib object.")
root = autotrackable.AutoTrackable()
path = pathlib.Path(tempfile.mkdtemp(prefix=self.get_temp_dir()))
save.save(root, path)
self.assertTrue(loader_impl.contains_saved_model(path))

test_load(path, use_cpp_bindings=use_cpp_bindings)
