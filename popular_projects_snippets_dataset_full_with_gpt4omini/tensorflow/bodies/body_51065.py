# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
model = autotrackable.AutoTrackable()
model.f = def_function.function(lambda: 3., input_signature=())
model.f()
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(model, save_dir)
self.assertAllClose({"output_0": 3.}, _import_and_infer(save_dir, {}))
