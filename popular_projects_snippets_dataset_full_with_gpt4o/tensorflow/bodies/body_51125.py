# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
with open(asset_path, "w") as f:
    f.write(label)

model = autotrackable.AutoTrackable()
model.asset = asset.Asset(asset_path)
model.fn = def_function.function(lambda: io_ops.read_file(model.asset))
self.assertEqual(label, model.fn().numpy().decode("utf-8"))

save.save(model, save_dir)
imported = load.load(save_dir)
self.assertEqual(label, imported.fn().numpy().decode("utf-8"))
