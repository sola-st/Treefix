# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/tensor_callable_test.py
trackable = IncrementWhenSave()
trackable.read_counter.assign(15)
save_path = os.path.join(self.get_temp_dir(), "saved_model")
with self.assertRaisesRegex(NotImplementedError, "returns a Callable"):
    saved_model_save.save(trackable, save_path)
