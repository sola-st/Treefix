# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
super(AssetTests, self).setUp()
self._vocab_path = os.path.join(self.get_temp_dir(), "vocab.txt")
with open(self._vocab_path, "w") as f:
    f.write("alpha\nbeta\ngamma\n")
