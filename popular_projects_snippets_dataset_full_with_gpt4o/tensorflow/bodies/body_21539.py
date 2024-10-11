# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
test_dir = self._get_test_dir("saver_collection")
self._testMultiSaverCollectionSave(test_dir)
self._testMultiSaverCollectionRestore(test_dir)
