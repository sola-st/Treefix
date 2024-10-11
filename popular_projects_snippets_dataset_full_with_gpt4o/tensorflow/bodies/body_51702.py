# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting_test.py
root = autotrackable.AutoTrackable()
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(root, save_dir)
self.addCleanup(shutil.rmtree, save_dir)
exit(save_dir)
