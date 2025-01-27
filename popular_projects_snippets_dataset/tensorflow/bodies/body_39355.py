# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
self._base_dir = os.path.join(self.get_temp_dir(), "saver_utils_test")
gfile.MakeDirs(self._base_dir)
