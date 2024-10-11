# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
model = autotrackable.AutoTrackable()
model.f = def_function.function(lambda: 3.)
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(model, save_dir)
