# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base_delegate_test.py
a = Wrapper(Inner(variables_lib.Variable(-15.0)))
self.evaluate([a.v.initializer])
self.assertEqual([-15], self.evaluate([a.v]))

test_dir = self.get_temp_dir()
saved_model_path = os.path.join(test_dir, "saved_model")
save.save(a, saved_model_path)

loaded = load.load(saved_model_path)
self.evaluate([loaded.v.initializer])
self.assertEqual([-15], self.evaluate([loaded.v]))
