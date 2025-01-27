# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
test_dir = self._get_test_dir("scoped_export_import")
ckpt_filename = "ckpt"
self._testScopedSave(test_dir, "exported_hidden1.pbtxt", ckpt_filename)
self._testScopedRestore(test_dir, "exported_hidden1.pbtxt",
                        "exported_new_hidden1.pbtxt", ckpt_filename)
