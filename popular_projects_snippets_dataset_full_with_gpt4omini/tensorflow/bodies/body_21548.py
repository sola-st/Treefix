# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
test_dir = self._get_test_dir("graph_extension")
# train.Saver and train.import_meta_graph are V1 only APIs.
with ops_lib.Graph().as_default():
    self._testGraphExtensionSave(test_dir)
    self._testGraphExtensionRestore(test_dir)
    self._testRestoreFromTrainGraphWithControlContext(test_dir)
