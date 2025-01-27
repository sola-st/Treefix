# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = checkpoint.Checkpoint(signatures=variables.Variable(1.))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
with self.assertRaisesRegex(ValueError, "del obj.signatures"):
    save.save(root, save_dir)
del root.signatures
save.save(root, save_dir)
