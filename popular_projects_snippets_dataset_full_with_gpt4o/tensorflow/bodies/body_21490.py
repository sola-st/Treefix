# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "cache_rereads")
# Save and reload one Variable named "var0".
self._SaveAndLoad("var0", 0.0, 1.0, save_path)
# Save and reload one Variable named "var1" in the same file.
# The cached readers should know to re-read the file.
self._SaveAndLoad("var1", 1.1, 2.2, save_path)
