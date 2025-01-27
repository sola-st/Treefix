# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
if use_cpp_bindings:
    self.skipTest("Cpp bindings do not support Tags.")
root = autotrackable.AutoTrackable()
path = tempfile.mkdtemp(prefix=self.get_temp_dir())
save.save(root, path)

with self.assertRaises(ValueError):
    load.load(path, tags=[tag_constants.EVAL])
load.load(path, tags=[tag_constants.SERVING])
load.load(path, tags=tag_constants.SERVING)
load.load(path, tags=set([tag_constants.SERVING]))
