# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
asset_path = os.path.join(self.get_temp_dir(), "asset")

def save_and_load(label):
    with open(asset_path, "w") as f:
        f.write(label)

    model = autotrackable.AutoTrackable()
    model.asset = asset.Asset(asset_path)
    model.fn = def_function.function(lambda: io_ops.read_file(model.asset))
    self.assertEqual(label, model.fn().numpy().decode("utf-8"))

    save.save(model, save_dir)
    imported = load.load(save_dir)
    self.assertEqual(label, imported.fn().numpy().decode("utf-8"))

save_and_load("first")
save_and_load("second")
