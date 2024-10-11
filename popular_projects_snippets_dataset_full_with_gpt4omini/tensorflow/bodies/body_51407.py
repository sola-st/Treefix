# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
root.vocab = asset.Asset(self._make_asset("contents"))
root.f = def_function.function(
    lambda: root.vocab.asset_path, input_signature=[]
)

original_output = root.f().numpy()

if cycles > 1:
    root = cycle(root, cycles - 1, use_cpp_bindings=use_cpp_bindings)
path = tempfile.mkdtemp(prefix=self.get_temp_dir())
save.save(root, path)

with ops.Graph().as_default():
    imported = test_load(path, use_cpp_bindings=use_cpp_bindings)
    imported_tensor = imported.f()
    with monitored_session.MonitoredSession() as sess:
        imported_output = sess.run(imported_tensor)
        self.assertLen(ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS), 1)
        self.assertNotEqual(original_output, imported_output)
        with open(imported_output, "r") as f:
            self.assertEqual("contents", f.read())
