# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.f = def_function.function(lambda x: 2. * x)
root.f(constant_op.constant(1.))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
with self.assertRaisesRegex(ValueError, "Expected a TensorFlow function"):
    save.save(root, save_dir, root.f)
