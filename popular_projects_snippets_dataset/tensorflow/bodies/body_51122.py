# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.f = def_function.function(
    lambda x: 2. * x,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
root.asset = asset.Asset(self._vocab_path)

export_dir = os.path.join(self.get_temp_dir(), "save_dir")
save.save(root, export_dir)
self.assertAllClose({"output_0": [0.2]},
                    _import_and_infer(export_dir, {"x": [0.1]}))
